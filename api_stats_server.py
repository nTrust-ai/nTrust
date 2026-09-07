#!/usr/bin/env python3
"""
nTrust.ai telemetry / stats API server (port 55127).

- Binds to 0.0.0.0 so external / host traffic is NOT dropped (localhost bind trap fix).
- Serves /api/stats and /health as JSON.

P0 directive: CEO Nedo / TASK-09986B / apr_3b6d06a9.
"""

import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "0.0.0.0"
PORT = 55127
STARTED_AT = time.time()


def stats_payload():
    return {
        "service": "ntrust-revenue-ops-telemetry",
        "status": "ok",
        "port": PORT,
        "bind": HOST,
        "uptime_seconds": round(time.time() - STARTED_AT, 2),
        "endpoints": ["/api/stats", "/health"],
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


class ApiHandler(BaseHTTPRequestHandler):
    server_version = "nTrustAPI/1.0"

    def _json(self, code, obj):
        body = json.dumps(obj, sort_keys=True).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in ("/api/stats", "/stats"):
            self._json(200, stats_payload())
            return
        if path in ("/health", "/healthz", "/api/health"):
            self._json(
                200,
                {
                    "status": "ok",
                    "service": "ntrust-revenue-ops-telemetry",
                    "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                },
            )
            return
        if path in ("/", ""):
            self._json(200, stats_payload())
            return
        self._json(404, {"error": "not_found", "path": path})

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))


if __name__ == "__main__":
    srv = ThreadingHTTPServer((HOST, PORT), ApiHandler)
    sys.stderr.write("nTrust telemetry API listening on %s:%d\n" % (HOST, PORT))
    sys.stderr.flush()
    srv.serve_forever()
