#!/usr/bin/env python3
"""
nTrust.ai MVP static SPA server (port 8085).

- Binds to 0.0.0.0 so external / host traffic is NOT dropped (localhost bind trap fix).
- Serves the built frontend from /app/data/orgs/org_ntrust/frontend/dist.
- SPA fallback: extension-less deep links (e.g. /dashboard, /about) return index.html (200).
- Directory listing is DISABLED (returns 403).

P0 directive: CEO Nedo / TASK-09986B / apr_3b6d06a9.
"""

import os
import sys
import posixpath
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = "/app/data/orgs/org_ntrust/frontend/dist"
INDEX = "index.html"
PORT = 8085
HOST = "0.0.0.0"

# File extensions that we treat as static assets (must exist or -> 404).
STATIC_EXT = {
    ".html",
    ".css",
    ".js",
    ".map",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".webp",
    ".woff",
    ".woff2",
    ".ttf",
    ".txt",
    ".xml",
    ".pdf",
    ".webmanifest",
}

MIME = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".ico": "image/x-icon",
    ".webp": "image/webp",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
    ".ttf": "font/ttf",
    ".txt": "text/plain; charset=utf-8",
    ".webmanifest": "application/manifest+json",
}


class SPAHandler(BaseHTTPRequestHandler):
    server_version = "nTrustMVP/1.0"

    def _send_file(self, path):
        try:
            with open(path, "rb") as f:
                data = f.read()
        except OSError:
            self.send_error(404, "Not Found")
            return
        ext = os.path.splitext(path)[1].lower()
        ctype = MIME.get(ext, "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.end_headers()
        self.wfile.write(data)

    def _resolve(self, raw_path):
        path = urllib.parse.unquote(raw_path.split("?", 1)[0].split("#", 1)[0])
        if path == "":
            path = "/"
        # Prevent path traversal
        path = posixpath.normpath(path)
        if not path.startswith("/"):
            path = "/" + path
        return path

    def do_GET(self):
        path = self._resolve(self.path)

        # Root -> index.html
        if path == "/":
            self._send_file(os.path.join(ROOT, INDEX))
            return

        ext = os.path.splitext(path)[1].lower()
        fs_path = os.path.join(ROOT, path.lstrip("/"))

        # If it's a real file, serve it.
        if os.path.isfile(fs_path):
            self._send_file(fs_path)
            return

        # If it's a directory, try index.html inside; else SPA fallback.
        if os.path.isdir(fs_path):
            idx = os.path.join(fs_path, INDEX)
            if os.path.isfile(idx):
                self._send_file(idx)
                return
            # Directory listing disabled -> SPA fallback (do NOT list)
            self._send_file(os.path.join(ROOT, INDEX))
            return

        # Extension-less deep link -> SPA fallback to index.html (200).
        if ext == "":
            self._send_file(os.path.join(ROOT, INDEX))
            return

        # Static asset that does not exist -> 404.
        self.send_error(404, "Not Found")

    def do_HEAD(self):
        self.do_GET()

    def list_directory(self, path):
        # Directory listing disabled.
        self.send_error(403, "Directory listing disabled")
        return None

    def log_message(self, fmt, *args):
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))


if __name__ == "__main__":
    os.chdir(ROOT)
    srv = ThreadingHTTPServer((HOST, PORT), SPAHandler)
    sys.stderr.write(
        "nTrust MVP SPA server listening on %s:%d root=%s\n" % (HOST, PORT, ROOT)
    )
    sys.stderr.flush()
    srv.serve_forever()
