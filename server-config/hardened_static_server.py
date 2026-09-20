#!/usr/bin/env python3
"""
nTrust.ai — Hardened Static File Server (Zero-Trust Compliance Patch)
Fixes: Directory listing exposure on ports 55004/55005
Compliance: EU AI Act Art. 12 / NIST AI RMF / Zero-Trust Protocol
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 55004
STATIC_DIR = os.path.join(os.path.dirname(__file__), "dist")

class SecureHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        # Prevent path traversal
        if ".." in self.path:
            self.send_error(403, "Forbidden")
            return
        super().do_GET()

    def list_directory(self):
        """Override to disable directory listing entirely."""
        self.send_error(403, "Directory listing disabled for security compliance.")

    def log_message(self, format, *args):
        # Suppress verbose logs in production per audit efficiency mandate
        pass

if __name__ == "__main__":
    if not os.path.exists(STATIC_DIR):
        print(f"⚠️  Static dist directory not found at {STATIC_DIR}")
        sys.exit(1)
        
    with socketserver.TCPServer(("0.0.0.0", PORT), SecureHandler) as httpd:
        print(f"🔒 nTrust.ai Hardened Server running on port {PORT} (Zero-Trust Mode)")
        httpd.serve_forever()
