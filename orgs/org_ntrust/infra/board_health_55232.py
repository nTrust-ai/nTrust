#!/usr/bin/env python3
"""Board-Test health endpoint :55232 (sanitized JSON). Restored 2026-09-06 per CEO directive."""
import json, http.server, socketserver, time
PORT = 55232
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"status": "healthy", "service": "ntrust-board-test",
                           "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, fmt, *a): pass
with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), H) as httpd:
    print(f"board-test health on 0.0.0.0:{PORT}", flush=True)
    httpd.serve_forever()
