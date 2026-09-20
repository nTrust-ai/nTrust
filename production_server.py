#!/usr/bin/env python3
"""nTrust Production Server v2 — Secure static file server with proper routing."""
import http.server, socketserver, json, os
from urllib.parse import urlparse

PORT = 8085
DOCROOT = "/app/data/orgs/org_ntrust/dashboard"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DOCROOT, **kw)
    
    def do_GET(self):
        p = urlparse(self.path).path
        
        if p == "/health" or p == "/api/health":
            data = {"status": "healthy", "service": "ntrust-production", "port": PORT}
            body = json.dumps(data).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)
            return
        
        if p == "/" or p == "":
            fpath = os.path.join(DOCROOT, "index.html")
            if os.path.isfile(fpath):
                self._serve(fpath, "text/html; charset=utf-8")
                return
        
        rel = urlparse(self.path).path.lstrip("/")
        if not rel:
            rel = "index.html"
        
        fpath = os.path.realpath(os.path.join(DOCROOT, rel))
        allowed = os.path.realpath(DOCROOT)
        
        if not fpath.startswith(allowed) or not os.path.isfile(fpath):
            alt_root = "/app/data/orgs/org_ntrust/www-catalog"
            alt_path = os.path.realpath(os.path.join(alt_root, rel))
            if alt_path.startswith(os.path.realpath(alt_root)) and os.path.isfile(alt_path):
                self._serve(alt_path)
                return
            body = json.dumps({"error": "not_found", "path": p}).encode()
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
            return
        
        self._serve(fpath)
    
    def _serve(self, filepath, default_ct="application/octet-stream"):
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            ext = os.path.splitext(filepath)[1].lower()
            ct_map = {".html": "text/html; charset=utf-8", ".css": "text/css", 
                        ".js": "application/javascript", ".json": "application/json"}
            ct = ct_map.get(ext, default_ct)
            self.send_response(200)
            self.send_header("Content-Type", ct)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            body = json.dumps({"error": "not_found"}).encode()
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
    
    def log_message(self, fmt, *args):
        pass

with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"nTrust Production serving on 0.0.0.0:{PORT} (DOCROOT={DOCROOT})")
    httpd.serve_forever()
