#!/usr/bin/env python3
"""nTrust Shield surface server — landing page + health (sanitized)."""

import http.server, socketserver, json, os
from urllib.parse import urlparse

PORT = int(os.environ.get("SHIELD_PORT", 7790))
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")


class ShieldHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        p = urlparse(self.path).path
        if p == "/health":
            body = json.dumps(
                {
                    "status": "healthy",
                    "service": "ntrust-shield",
                    "port": PORT,
                    "compliance_framework": "NIST AI RMF / EU AI Act",
                }
            ).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif p in ("/", "/index.html"):
            try:
                with open(ROOT, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                self.send_error(404, "Not Found")
        else:
            self.send_error(404, "Not Found")

    def log_message(self, fmt, *args):
        pass


def run():
    with socketserver.TCPServer(("0.0.0.0", PORT), ShieldHandler) as httpd:
        print(f"nTrust Shield surface serving 0.0.0.0:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    run()
