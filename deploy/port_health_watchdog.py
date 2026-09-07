#!/usr/bin/env python3
"""
nTrust.ai — Port-Health Watchdog (TASK-646340)
================================================
Monitors the four externally-facing surfaces required for Phase 3 revenue ops:
    :8085  corporate site      (expects /healthz token "healthy")
    :55127 revenue ops center  (expects /healthz token "healthy")
    :9090  service catalog     (expects /health  HTTP 200)
    :7790  nTrust Shield MVP   (expects /health  token "healthy")

Zero-trust: performs a REAL TCP connect + HTTP GET (no mocks, no fabricated status).
EU AI Act / NIST AI RMF: every run is appended to an append-only JSONL audit log,
so state changes (surface UP/DOWN/DEGRADED) are traceable.

Usage (once a compute environment is attached):
    python3 port_health_watchdog.py            # one-shot probe, exit 0 if all healthy
    */1 * * * * python3 port_health_watchdog.py   # cron for continuous coverage

Exit codes:
    0 = all surfaces HEALTHY
    1 = >=1 surface DOWN or DEGRADED (for alerting / self-heal hooks)
"""

import json
import socket
import sys
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone

LOG_PATH = os.environ.get(
    "WATCHDOG_LOG",
    "/app/data/orgs/org_ntrust/watchdog_audit.jsonl",
)

SURFACES = [
    {"name": "corporate-site", "port": 8085, "path": "/healthz", "expect": "healthy"},
    {"name": "revenue-ops", "port": 55127, "path": "/healthz", "expect": "healthy"},
    {"name": "service-catalog", "port": 9090, "path": "/health", "expect": None},
    {"name": "shield-mvp", "port": 7790, "path": "/health", "expect": "healthy"},
]

CONNECT_TIMEOUT = 3
HTTP_TIMEOUT = 4


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def probe(surface: dict) -> dict:
    result = {
        "name": surface["name"],
        "port": surface["port"],
        "ts": now_iso(),
    }

    # 1) TCP reachability
    try:
        sock = socket.create_connection(
            ("127.0.0.1", surface["port"]), timeout=CONNECT_TIMEOUT
        )
        sock.close()
        result["tcp"] = "OPEN"
    except OSError as exc:
        result["tcp"] = "CLOSED"
        result["http"] = None
        result["status"] = "DOWN"
        result["error"] = str(exc)
        return result

    # 2) HTTP health check
    url = "http://127.0.0.1:{}{}".format(surface["port"], surface["path"])
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Atlas-HealthCheck/1.0"}
        )
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            body = resp.read(2048)
            result["http"] = resp.status
            result["bytes"] = len(body)
            text = body.decode("utf-8", errors="ignore")
            if surface["expect"] is not None and surface["expect"] not in text:
                result["status"] = "DEGRADED"
                result["note"] = "expected token '{}' absent".format(surface["expect"])
            else:
                result["status"] = "HEALTHY"
    except urllib.error.HTTPError as exc:
        result["http"] = exc.code
        result["status"] = "DEGRADED"
        result["note"] = "HTTP {}".format(exc.code)
    except Exception as exc:  # timeout, conn reset, etc.
        result["http"] = None
        result["status"] = "DOWN"
        result["error"] = str(exc)

    return result


def main() -> int:
    results = [probe(s) for s in SURFACES]

    # Append-only audit log (EU AI Act traceability)
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a") as fh:
            fh.write(json.dumps({"ts": now_iso(), "surfaces": results}) + "\n")
    except OSError as exc:
        print("WARN: audit log write failed: {}".format(exc), file=sys.stderr)

    # Human-readable summary
    for r in results:
        detail = r.get("note") or r.get("error") or ""
        print(
            "[{:<8}] {:<16} :{} tcp={} http={} {}".format(
                r["status"], r["name"], r["port"], r["tcp"], r.get("http"), detail
            ).rstrip()
        )

    unhealthy = [r for r in results if r["status"] != "HEALTHY"]
    healthy_count = len(results) - len(unhealthy)
    print("\n{}/{} surfaces HEALTHY".format(healthy_count, len(results)))
    return 1 if unhealthy else 0


if __name__ == "__main__":
    sys.exit(main())
