#!/usr/bin/env python3
"""
nTrust.ai Port-Health Watchdog v1.0 (Atlas — Infrastructure & DevOps Director)
Monitors revenue-critical host-published surfaces:
  55127 (Dashboard) | 9090 (Service Catalog) | 7790 (nTrust Shield MVP) | 8085 (Corporate SPA)
Usage: python3 port_health_watchdog.py [--json]
Exit 0 = all healthy; 1 = one or more surfaces DOWN (for cron alerting).
Empirical baseline 2026-09-04: 55127->200(13253B) 9090->200(7597B) 7790->200 8085->200 (host.docker.internal vantage).
Refs: RAID-C44912 (watchdog stale), RAID-382414 (directory-listing regression), TASK-646340, TASK-968B4B.
"""
import json, sys, urllib.request

SURFACES = [
    {"name": "55127-dashboard", "host_candidates": ["host.docker.internal", "localhost"], "port": 55127, "path": "/"},
    {"name": "9090-catalog",     "host_candidates": ["host.docker.internal", "localhost"], "port": 9090, "path": "/"},
    {"name": "7790-shield",      "host_candidates": ["host.docker.internal", "localhost"], "port": 7790, "path": "/"},
    {"name": "8085-corporate",   "host_candidates": ["host.docker.internal", "localhost"], "port": 8085, "path": "/"},
]
HEALTH_PATHS = [("/health", 7790), ("/healthz", 8085)]

def probe(host, port, path="/", timeout=6):
    try:
        r = urllib.request.urlopen(f"http://{host}:{port}{path}", timeout=timeout)
        b = r.read()
        return {"up": True, "status": r.status, "bytes": len(b), "server": r.headers.get("Server", "")}
    except Exception as e:
        return {"up": False, "error": f"{type(e).__name__}: {e}"}

def main():
    results = {}
    for s in SURFACES:
        outcome = None
        for h in s["host_candidates"]:
            outcome = probe(h, s["port"], s["path"])
            if outcome["up"]:
                outcome["host"] = h
                break
        results[s["name"]] = outcome or {"up": False, "error": "no host reachable"}
    for path, port in HEALTH_PATHS:
        results[f"{port}{path}"] = probe("host.docker.internal", port, path)
    all_up = all(v.get("up") for v in results.values())
    if "--json" in sys.argv:
        print(json.dumps(results, indent=2))
    else:
        for k, v in results.items():
            state = "UP  " if v.get("up") else "DOWN"
            detail = f"HTTP {v.get('status')} ({v.get('bytes')}B) {v.get('server','')}".strip() if v.get("up") else v.get("error", "?")
            print(f"[{state}] {k:20s} -> {detail}")
    print(f"\nOVERALL: {'HEALTHY' if all_up else 'DEGRADED'}")
    sys.exit(0 if all_up else 1)

if __name__ == "__main__":
    main()
