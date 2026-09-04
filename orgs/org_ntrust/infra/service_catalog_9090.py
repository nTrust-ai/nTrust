#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import time
import socket

start_time = time.time()

# Allow address reuse to free up the port quickly
class ReuseAddrHTTPServer(HTTPServer):
    allow_reuse_address = True

class CatalogHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/health', '/api/health']:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = json.dumps({'status': 'healthy', 'uptime': time.time() - start_time})
            self.wfile.write(response.encode())
        elif self.path in ['/', '/index', '/catalog']:
            catalog = {
                'service': 'nTrust.ai Service Catalog',
                'products': [
                    {'id': 'PROD-DCCCF5', 'name': 'nTrust Shield'},
                    {'id': 'PROD-SUN001', 'name': 'SUN-Token NFC Security'}
                ]
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(catalog).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Suppress logging for cleaner output

if __name__ == '__main__':
    server = ReuseAddrHTTPServer(('0.0.0.0', 9090), CatalogHandler)
    print(f"🚀 Service Catalog running on http://0.0.0.0:9090", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        server.shutdown()
