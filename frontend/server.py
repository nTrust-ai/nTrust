#!/usr/bin/env python3
"""
Simple HTTP Server for nTrust.ai Dashboard MVP
Serves static files from the current directory on port 8085
Bound to 0.0.0.0 for external access compliance
"""

import http.server
import socketserver
import os

PORT = 8085
DIRECTORY = '/app/data/orgs/org_ntrust/frontend'

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        # Suppress default logging for cleaner output
        pass

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving nTrust.ai Dashboard MVP at http://0.0.0.0:{PORT}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()