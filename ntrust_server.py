#!/usr/bin/env python3
"""nTrust.ai Static Site Server for Phase 3 Revenue MVP."""
import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8085
DIRECTORY = "/app/data/workspace"

os.chdir(DIRECTORY)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        pass  # Suppress verbose logging

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"🚀 nTrust.ai MVP serving on 0.0.0.0:{PORT}")
    httpd.serve_forever()
