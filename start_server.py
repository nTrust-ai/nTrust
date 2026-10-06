#!/usr/bin/env python3
"""nTrust.ai — TrustGuard MVP & Executive Bio Server with auto-port fallback"""
import http.server
import socketserver
import os

PORTS_TO_TRY = [55128, 55129, 49152, 49200, 39000, 39001, 40000]
DIST_DIR = "/app/dist"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

for port in PORTS_TO_TRY:
    try:
        with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
            print(f"✅ Serving nTrust.ai Executive Bio + TrustGuard on port {port}")
            httpd.serve_forever()
            break
    except OSError as e:
        print(f"⚠️ Port {port} unavailable: {e}")

print("❌ No available ports found in list")
