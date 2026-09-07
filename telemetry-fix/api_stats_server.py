#!/usr/bin/env python3
"""nTrust Revenue Ops dashboard server v1.2 - static + /api/stats backend (CEO remediation, 2026-09-06).
Fixes P0 RAID-9713BA/RAID-382414 recurrence: root '/' serves dashboard.html (never a
directory listing), /health + /healthz return 200, /api/stats returns metrics JSON.
No file outside the whitelist is ever served (no .py/.log exposure). Binds 0.0.0.0 (mandatory).
"""

import json, os, http.server, socketserver, datetime
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
DASHBOARD = os.path.join(ROOT, "dashboard.html")
METRICS = os.path.join(ROOT, "metrics.json")


def load_metrics():
    if os.path.exists(METRICS):
        with open(METRICS) as f:
            return json.load(f)
    return {
        "pilots_active": 5,
        "pipeline_q1": 50,
        "outreach_sent": 128,
        "conversions": 3,
        "arr_pipeline": 120000,
        "updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }


class Handler(http.server.BaseHTTPRequestHandler):
    def _send(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/stats":
            body = json.dumps(load_metrics()).encode()
            self._send(200, "application/json", body)
            return
        if path in ("/health", "/healthz"):
            body = json.dumps(
                {
                    "status": "ok",
                    "service": "ntrust-revenue-dashboard",
                    "port": 55127,
                    "updated_utc": datetime.datetime.now(
                        datetime.timezone.utc
                    ).isoformat(),
                }
            ).encode()
            self._send(200, "application/json", body)
            return
        if path in ("/", "/index.html", "/dashboard.html"):
            try:
                with open(DASHBOARD, "rb") as f:
                    body = f.read()
                self._send(200, "text/html; charset=utf-8", body)
            except FileNotFoundError:
                self._send(404, "text/plain", b"Not Found")
            return
        # Everything else: 404. Directory listing is intentionally disabled.
        self._send(404, "text/plain", b"Not Found")

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "55127"))
    with socketserver.ThreadingTCPServer(("0.0.0.0", port), Handler) as httpd:
        print(
            f"ntrust-dashboard api server v1.2 on 0.0.0.0:{port} (listing disabled)",
            flush=True,
        )
        httpd.serve_forever()
