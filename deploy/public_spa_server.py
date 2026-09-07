#!/usr/bin/env python3
"""nTrust.ai public website SPA server.

Binds 0.0.0.0:8085 (Localhost Bind Trap compliant). Serves the sanitized
customer-facing public site with SPA deep-route fallback. Pure stdlib.
"""

import os
import socketserver
from http.server import SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8085

ORG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(ORG_ROOT, "public_site")
INDEX_PATH = os.path.join(SITE_ROOT, "index.html")


class PublicSiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_ROOT, **kwargs)

    def _send_index(self):
        try:
            with open(INDEX_PATH, "rb") as fh:
                body = fh.read()
        except FileNotFoundError:
            body = (
                b"<html><body><h1>nTrust.ai</h1><p>Site unavailable.</p></body></html>"
            )
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/") or "/"
        if path == "/index.html" or path == "/":
            return self._send_index()
        # Attempt static file first, then SPA fallback
        candidate = os.path.normpath(os.path.join(SITE_ROOT, path.lstrip("/")))
        if candidate.startswith(SITE_ROOT) and os.path.isfile(candidate):
            return super().do_GET()
        return self._send_index()

    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args), flush=True)


class ThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    print(
        "nTrust.ai public site server starting on %s:%d (root=%s)"
        % (HOST, PORT, SITE_ROOT),
        flush=True,
    )
    ThreadingServer((HOST, PORT), PublicSiteHandler).serve_forever()
