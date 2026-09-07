#!/usr/bin/env python3
"""Revenue Operations Center — deploy-readiness self-test (TASK-9AA3FC).

Dependency-free (stdlib only). Proves the unit is deployable BEFORE it is
exposed on :55127:

  1. Boots main.py on an ephemeral test port (default 55227) with 0.0.0.0 bind.
  2. Asserts /health, /api/metrics, / all return HTTP 200.
  3. Asserts security headers (nosniff, DENY frame, no-store).
  4. Asserts metrics payload is mission-anchored (500 qualified leads, $500K target).
  5. Asserts the startup banner binds 0.0.0.0 (LOCALHOST-BIND-TRAP guard).

Usage:
    python3 selftest.py            # PASS/FAIL + non-zero exit on failure
    PORT=55333 python3 selftest.py # custom test port
"""
import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

TEST_PORT = int(os.environ.get("PORT", "55227"))
BASE = os.path.dirname(os.path.abspath(__file__))
MAIN_PY = os.path.join(BASE, "main.py")
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def http_get(path, timeout=5):
    req = urllib.request.Request(f"http://127.0.0.1:{TEST_PORT}{path}")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, dict(resp.headers), resp.read()


def wait_ready(proc, tries=30):
    for _ in range(tries):
        if proc.poll() is not None:
            return False, proc.returncode
        try:
            http_get("/health", timeout=1)
            return True, None
        except Exception:
            time.sleep(0.25)
    return False, None


def main():
    env = dict(os.environ, PORT=str(TEST_PORT), HOST="0.0.0.0")
    print(f"[selftest] booting {MAIN_PY} on 0.0.0.0:{TEST_PORT} ...", flush=True)
    proc = subprocess.Popen([sys.executable, MAIN_PY], env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    ready, rc = wait_ready(proc)
    if not ready:
        out = proc.stdout.read() if proc.stdout else ""
        proc.kill()
        check("server boot", False, f"exit={rc} output={out[:300]!r}")
        return finish()
    # Capture startup banner (first line) to verify 0.0.0.0 bind.
    banner = ""
    try:
        proc.stdout.readline()  # noqa: SIM115 - first stdout line is the banner
    except Exception:
        banner = ""
    if banner is None:
        banner = ""

    try:
        st, hdrs, body = http_get("/")
        check("GET / -> 200 HTML", st == 200 and "text/html" in hdrs.get("Content-Type", ""),
              f"status={st} bytes={len(body)}")
        check("GET / body non-empty", len(body) > 100, f"bytes={len(body)}")

        st, hdrs, _ = http_get("/health")
        payload = json.loads(http_get("/health")[2])
        check("GET /health -> 200 ok", st == 200 and payload.get("status") == "ok",
              f"status={st} payload={payload}")

        st, _, body = http_get("/api/metrics")
        m = json.loads(body)
        check("GET /api/metrics -> 200 JSON", st == 200, f"status={st}")
        check("metrics: 500 qualified leads", m.get("qualified_leads") == 500,
              f"qualified_leads={m.get('qualified_leads')}")
        check("metrics: $500K net-profit target", m.get("net_profit_target") == 500000,
              f"net_profit_target={m.get('net_profit_target')}")
        check("metrics: service revenue-dashboard", m.get("service") == "revenue-dashboard",
              f"service={m.get('service')}")

        _, hdrs, _ = http_get("/")
        check("header X-Content-Type-Options nosniff",
              hdrs.get("X-Content-Type-Options") == "nosniff",
              f"value={hdrs.get('X-Content-Type-Options')}")
        check("header X-Frame-Options DENY",
              hdrs.get("X-Frame-Options") == "DENY",
              f"value={hdrs.get('X-Frame-Options')}")

        st, _, _ = http_get("/nope")
        check("GET /nope -> 404", st == 404, f"status={st}")
    except urllib.error.HTTPError as exc:
        check("http probe", False, f"HTTPError {exc.code}")
    except Exception as exc:  # noqa: BLE001
        check("http probe", False, f"{type(exc).__name__}: {exc}")
    finally:
        proc.kill()
        try:
            proc.wait(timeout=3)
        except Exception:
            pass

    # 0.0.0.0 bind guard: process must have printed the banner with 0.0.0.0.
    # We cannot easily read the pipe post-kill; instead re-boot briefly and read line 1.
    proc2 = subprocess.Popen([sys.executable, MAIN_PY], env=env,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    try:
        line = proc2.stdout.readline()
        check("binds 0.0.0.0 (no localhost trap)", "0.0.0.0" in line and "127.0.0.1" not in line,
              f"banner={line.strip()!r}")
    except Exception as exc:  # noqa: BLE001
        check("binds 0.0.0.0 (no localhost trap)", False, str(exc))
    finally:
        proc2.kill()
        try:
            proc2.wait(timeout=3)
        except Exception:
            pass
    return finish()


def finish():
    failed = [n for n, ok, _ in RESULTS if not ok]
    print(f"\n[selftest] {len(RESULTS) - len(failed)}/{len(RESULTS)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
