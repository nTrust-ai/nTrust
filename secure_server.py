#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT_8085 = 8085
PORT_55127 = 55127
WEB_ROOT = "/app/data/orgs/org_ntrust/mvp/shield"

# Create a dummy index.html if it doesn't exist to prevent directory listings
INDEX_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>nTrust.ai | Secure Access</title><style>body{margin:0;font-family:system-ui;background:#0f172a;color:#f8fafc;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center}.card{background:#1e293b;padding:3rem;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,.5)}.h1{font-size:2.5rem;margin-bottom:.5rem;color:#38bdf8}.p{color:#94a3b8;font-size:1.1rem;margin-bottom:1.5rem}.btn{padding:.75rem 1.5rem;background:#2563eb;color:#fff;border-radius:8px;text-decoration:none;font-weight:600;cursor:pointer}</style></head><body><div class="card"><h1>nTrust.ai</h1><p>Enterprise AI Cybersecurity & Autonomous Governance Portal</p><p>Status: Phase 3 Profitability Scaling Active</p><button class="btn" onclick="window.location.href='/dashboard'">Enter Pilot Dashboard</button></div></body></html>"""

os.makedirs(WEB_ROOT, exist_ok=True)
with open(os.path.join(WEB_ROOT, 'index.html'), 'w') as f:
    f.write(INDEX_HTML)

class SecureHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_ROOT, **kwargs)
    
    def log_message(self, format, *args):
        pass  # Suppress logs for performance
    
    def list_directory(self, path):
        self.send_error(403, "Directory listing forbidden for security.")

def run_server(port):
    with socketserver.TCPServer(("0.0.0.0", port), SecureHandler) as httpd:
        print(f"Serving on 0.0.0.0:{port} -> {WEB_ROOT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server(PORT_8085)
