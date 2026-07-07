#!/usr/bin/env python3
"""nTrust.ai Phase 1 MVP Dashboard — Production-Grade Sandbox Server"""
import http.server
import socketserver
import json
import os
from urllib.parse import urlparse

PORT = int(os.environ.get("MVP_PORT", 9021))

class nTrustHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            resp = {"status": "healthy", "service": "nTrust.ai MVP Dashboard", "phase": "1", "uptime_ms": 0}
            self.wfile.write(json.dumps(resp).encode())
        elif parsed_path.path == '/api/metrics':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            resp = {"active_users": 1, "sla_target": "99.9%", "pilot_status": "ready", "compliance": "NIST AI RMF / EU HITL"}
            self.wfile.write(json.dumps(resp).encode())
        else:
            super().do_GET()

    def log_message(self, format, *args):
        pass

def run():
    with socketserver.TCPServer(("0.0.0.0", PORT), nTrustHandler) as httpd:
        print(f"🚀 nTrust MVP Dashboard serving on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run()