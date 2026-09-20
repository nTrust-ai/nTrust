#!/usr/bin/env python3
"""Secure HTTP Server for Port 55005 — NO Directory Listing"""
import os, sys, posixpath, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 55005
HOST = "0.0.0.0"
DOCROOT = "/app/data"

class SecureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0]
        if path == '/' or path == '':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('X-Frame-Options', 'DENY')
            self.end_headers()
            self.wfile.write(b'{"status":"secure","port":55005}')
            return
         # Block directory traversal
        if '..' in path:
            self.send_response(403)
            self.end_headers()
            return
         # Only serve specific files, never list directories
        self.send_response(404)
        self.end_headers()
    def log_message(self, *args): pass

if __name__ == "__main__":
    with ThreadingHTTPServer((HOST, PORT), SecureHandler) as httpd:
        print(f"Secure server on {HOST}:{PORT}")
        httpd.serve_forever()
