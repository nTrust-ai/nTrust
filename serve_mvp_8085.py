#!/usr/bin/env python3
"""
nTrust.ai Phase 3 MVP Static Server - Port 8085
Serves static files securely with directory listing DISABLED.
Zero-trust compliant: No auto-indexing, proper MIME types, security headers.
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os, mimetypes, json

# Set correct MIME types for React SPA
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

class SecureStaticHandler(SimpleHTTPRequestHandler):
    """Serves static files WITHOUT directory listing."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='/app/data/prod/www', **kwargs)
    
    def log_message(self, format, *args):
        # Suppress noisy logs
        pass
    
    def list_directory(self, *args):
        """Override: Return 403 Forbidden instead of listing directory."""
        self.send_error(403, "Directory listing disabled for security")
    
    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Cache-Control', 'public, max-age=3600')
        super().end_headers()

class HealthCheckHandler(SimpleHTTPRequestHandler):
    """Provides health endpoint for the board."""
    directory = '/app/data/prod/www'
    
    def do_GET(self):
        if self.path in ['/health', '/api/health']:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            health = {
                'status': 'healthy',
                'service': 'nTrust.ai Phase 3 MVP',
                'port': 8085,
                'timestamp': '2026-09-20T06:03:07Z',
                'version': '1.0.0'
            }
            self.wfile.write(json.dumps(health).encode())
        else:
            super().do_GET()

def run_server():
    server = HTTPServer(('0.0.0.0', 8085), SecureStaticHandler)
    print("🚀 nTrust.ai MVP Server running on http://0.0.0.0:8085", flush=True)
    server.serve_forever()

if __name__ == '__main__':
    run_server()
