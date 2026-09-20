#!/usr/bin/env python3
"""Explicit 0.0.0.0 static server for canonical dist (Weaver empirical verification)."""
import http.server, socketserver, os, sys

ROOT = "/app/data/frontend/dist"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8099

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, fmt, *args):
        sys.stderr.write("REQ %s\n" % (fmt % args))

with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), H) as httpd:
    httpd.allow_reuse_address = True
    sys.stderr.write("LISTENING 0.0.0.0:%d root=%s\n" % (PORT, ROOT))
    sys.stderr.flush()
    httpd.serve_forever()
