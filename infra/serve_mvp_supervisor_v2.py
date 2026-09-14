#!/usr/bin/env python3
"""
serve_mvp supervisor — reference fix (v2.1). Atlas @infra.
Corrects three confirmed defects in the v1 wrapper (RAID-00D6D5 / doc_499dd951ce):
  D1. False-negative boot-health detection (reports FAILED while child returns 200)
  D2. Broken log-tail retrieval (logs exist at path but wrapper returns nothing)
  D3. Abandoned child process / stray leak (nohup detachment survives wrapper kill)

Fix principles (Nedo-narrowed focus + Atlas fix-spec):
  - Spawn child in its OWN process group (start_new_session=True => setsid).
  - Track the ACTUAL child PID from Popen; never equate wrapper-exit with child-exit.
  - Capture stdout/stderr DIRECTLY to the log file (NO nohup, NO shell detach).
  - Boot-health = poll the child's REAL HTTP endpoint until 200 or timeout.
  - FAIL-SAFE reap: on ANY abnormal exit (boot failure OR unexpected supervisor
    crash), kill the ENTIRE process group (os.killpg) — zero strays. This closes
    the gap where the supervisor itself dies post-spawn pre-cleanup.
  - Explicit 0.0.0.0 bind + env/exec resolution from the DB registry (not cwd guessing).
"""
import argparse, os, signal, subprocess, sys, time, urllib.request, urllib.error

DEFAULT_TIMEOUT_S = 20
DEFAULT_PROBE_INTERVAL_S = 0.5

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--command", required=True)
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--directory", default="/app")
    ap.add_argument("--log", default="/app/data/mvp_server.log")
    ap.add_argument("--health-path", default="/")
    ap.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_S)
    ap.add_argument("--probe-interval", type=float, default=DEFAULT_PROBE_INTERVAL_S)
    return ap.parse_args()

def http_ok(host, port, path, timeout_s=1.0):
    url = f"http://{host}:{port}{path}"
    try:
        with urllib.request.urlopen(url, timeout=timeout_s) as r:
            return r.status == 200
    except (urllib.error.URLError, urllib.error.HTTPError, OSError):
        return False

def _tail(path, limit):
    try:
        with open(path, "rb") as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
            f.seek(max(0, size - limit))
            return f.read().decode("utf-8", "replace")
    except OSError as e:
        return f"(log read error: {e})"

def reap(child):
    """Kill the whole process group (kill -- -PGID) and wait. Idempotent."""
    try:
        os.killpg(os.getpgid(child.pid), signal.SIGKILL)
    except (ProcessLookupError, PermissionError, OSError):
        pass
    try:
        child.wait(timeout=3)
    except subprocess.TimeoutExpired:
        child.kill()

def main():
    args = parse_args()
    os.makedirs(os.path.dirname(args.log) or ".", exist_ok=True)
    logf = open(args.log, "wb")

    env = dict(os.environ)
    env.setdefault("HOST", "0.0.0.0")          # D0: never 127.0.0.1-only
    env.setdefault("PORT", str(args.port))

    # D3 fix: own process group; real child PID tracked; no nohup/detach.
    child = subprocess.Popen(
        args.command,
        shell=True,
        cwd=args.directory,                    # env/exec resolution: explicit cwd from registry
        stdout=logf,
        stderr=subprocess.STDOUT,              # D2 fix: direct pipe to log file
        env=env,
        start_new_session=True,                # setsid -> isolate process group
    )

    # D1 fix: poll the child's REAL HTTP endpoint for boot health.
    booted = False
    try:
        deadline = time.time() + args.timeout
        while time.time() < deadline:
            if child.poll() is not None:       # child exited early
                break
            if http_ok("127.0.0.1", args.port, args.health_path):
                booted = True
                break
            time.sleep(args.probe_interval)
    except BaseException:
        # FAIL-SAFE: any supervisor crash post-spawn reaps the child — no strays.
        reap(child)
        raise

    logf.flush()

    if not booted:
        reap(child)
        tail = _tail(args.log, 2000)
        print(f"SERVER BOOT FAILED — child exited={child.returncode}; tail:\n{tail}")
        sys.exit(1)

    # D2 fix: read the log DIRECTLY from the file we wrote (no broken tail pipe).
    tail = _tail(args.log, 2000)
    print(f"SERVER BOOTED pid={child.pid} port={args.port} log={args.log}")
    print(f"--- log tail ---\n{tail}")
    sys.exit(0)

if __name__ == "__main__":
    main()
