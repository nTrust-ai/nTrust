#!/usr/bin/env python3
"""nTrust.ai Revenue & Security Intelligence Dashboard server.

Binds 0.0.0.0:55127 (Localhost Bind Trap compliant). Serves the sanitized
board-verified dashboard artifact with health and stats API endpoints and
SPA deep-route fallback. Pure stdlib, no bash required.
"""

import json
import os
import socketserver
from http.server import SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 55127
SERVICE = "ntrust-revenue-ops"

ORG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ORG_ROOT, "revenue-dashboard", "dist", "index.html")

STATS = {
    "threats_mitigated": 1248,
    "compliance_score": 98.5,
    "deployments": 4,
    "uptime": 99.98,
}
JOBS = {"jobs": [], "status": "idle"}


class DashboardHandler(SimpleHTTPRequestHandler):
    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_index(self):
        try:
            with open(INDEX_PATH, "rb") as fh:
                body = fh.read()
        except FileNotFoundError:
            body = b"<html><body><h1>nTrust.ai</h1><p>Dashboard unavailable.</p></body></html>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/") or "/"
        if path == "/health":
            return self._send_json(
                {"status": "healthy", "service": SERVICE, "port": PORT}
            )
        if path == "/healthz":
            return self._send_json({"status": "healthy", "service": SERVICE})
        if path == "/api/stats":
            return self._send_json(STATS)
        if path == "/api/jobs":
            return self._send_json(JOBS)
        if path in ("/", "/dashboard", "/revenue", "/index.html"):
            return self._send_index()
        # SPA deep-route fallback
        return self._send_index()

    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args), flush=True)


class ThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    print(
        "nTrust.ai dashboard server starting on %s:%d (index=%s)"
        % (HOST, PORT, INDEX_PATH),
        flush=True,
    )
    ThreadingServer((HOST, PORT), DashboardHandler).serve_forever()
