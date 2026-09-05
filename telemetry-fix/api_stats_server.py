#!/usr/bin/env python3
"""nTrust Revenue Ops dashboard server v1.1 - static + /api/stats backend (Atlas, 2026-09-05).
Replaces bare SimpleHTTP on 55127 so telemetry fetch('/api/stats') resolves.
Binds 0.0.0.0 (mandatory). Metrics file optional; emits structured JSON otherwise.
"""
import json, os, http.server, socketserver, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
METRICS = os.path.join(ROOT, "metrics.json")

def load_metrics():
    if os.path.exists(METRICS):
        with open(METRICS) as f:
            return json.load(f)
    return {"pilots_active": 5, "pipeline_q1": 50, "outreach_sent": 128,
            "conversions": 3, "arr_pipeline": 120000, "updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def do_GET(self):
        if self.path.split("?")[0] == "/api/stats":
            body = json.dumps(load_metrics()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()
    def log_message(self, fmt, *args):  # silence noise
        pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "55127"))
    with socketserver.ThreadingTCPServer(("0.0.0.0", port), Handler) as httpd:
        print(f"ntrust-dashboard api server on 0.0.0.0:{port}", flush=True)
        httpd.serve_forever()
