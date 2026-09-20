#!/usr/bin/env python3
"""nTrust Production Server — Multi-service HTTP server with security hardening."""
import http.server, socketserver, json, os, sys
from urllib.parse import urlparse

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8085
# Serve from dashboard (primary) or www-catalog (fallback)
DOCROOT = "/app/data/orgs/org_ntrust/dashboard"

class SecureHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DOCROOT, **kw)
    
    def _send_json(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.end_headers()
        self.wfile.write(body)
    
    def do_GET(self):
        p = urlparse(self.path).path
        if p == "/health":
            return self._send_json(200, {
                "status": "healthy",
                "service": "ntrust-production",
                "port": PORT,
                "uptime": "active"
            })
        elif p == "/api/health":
            return self._send_json(200, {
                "status": "active",
                "version": "3.1.0",
                "mvp_gate": "live"
            })
        # Safe static resolution — no directory listing
        rel = p.lstrip("/")
        if not rel or rel.endswith("/"):
            rel = rel + "index.html"
        fs = os.path.realpath(os.path.join(DOCROOT, rel))
        allowed = os.path.realpath(DOCROOT)
        if not fs.startswith(allowed) or not os.path.isfile(fs):
            # Check www-catalog fallback
            alt_root = "/app/data/orgs/org_ntrust/www-catalog"
            alt_fs = os.path.realpath(os.path.join(alt_root, rel))
            if alt_fs.startswith(os.path.realpath(alt_root)) and os.path.isfile(alt_fs):
                return self._serve_file(alt_fs)
            return self._send_json(404, {"error": "not_found"})
        return self._serve_file(fs)
    
    def _serve_file(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                body = f.read()
            ext = os.path.splitext(filepath)[1].lower()
            ct = "application/octet-stream"
            if ext == ".html": ct = "text/html; charset=utf-8"
            elif ext == ".css": ct = "text/css"
            elif ext == ".js": ct = "application/javascript"
            self.send_response(200)
            self.send_header("Content-Type", ct)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self._send_json(404, {"error": "not_found"})
    
    def log_message(self, fmt, *args):
        pass  # Suppress noisy logs

def run():
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), SecureHandler) as httpd:
        print(f"nTrust Production serving on 0.0.0.0:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run()
