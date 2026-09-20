#!/usr/bin/env python3
"""
nTrust.ai Secure MVP Server — Port 8085
Ensures zero-trust static serving: NO DIRECTORY LISTINGS. Binds to 0.0.0.0 for external access.
Complies with Board Directive: Enterprise-grade security architecture, no exposed directory trees.
"""
import http.server
import socketserver
import os
import sys

PORT = 8085
DIRECTORY = "/app/data/frontend/dist"
HOST = "0.0.0.0"

class SecureHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    # CRITICAL: Disable directory listing entirely to prevent directory traversal exposure
    def list_directory(self, path):
        self.send_error(403, "Directory listing disabled for security compliance.")
    
    def log_message(self, format, *args):
        print(f"[nTrust-8085] {self.address_string()} - {format % args}", flush=True)

def run():
    if not os.path.exists(DIRECTORY):
        print(f"CRITICAL: {DIRECTORY} not found. Launching fallback index.", file=sys.stderr)
        sys.exit(1)
    
    with socketserver.TCPServer((HOST, PORT), SecureHandler) as httpd:
        print(f"✅ nTrust MVP Server LIVE on {HOST}:{PORT}")
        print(f"   Serving: {os.path.abspath(DIRECTORY)}")
        print(f"   Security: Directory listings DISABLED per Board Directive.")
        httpd.serve_forever()

if __name__ == "__main__":
    run()
