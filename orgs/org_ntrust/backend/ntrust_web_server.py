#!/usr/bin/env python3
"""nTrust corporate web server - static canonical site + POST /api/contact lead capture.
Replacement for ntrust_web_server.py lost with pruned env_ee237d41 (2026-09-04).
Usage: python3 ntrust_web_server.py [DOCROOT] [PORT]
Sanitized. Binds 0.0.0.0 explicitly.
"""
import http.server, socketserver, json, os, sys, time, hashlib
from urllib.parse import urlparse, unquote

DOCROOT = sys.argv[1] if len(sys.argv) > 1 else "/app/data/frontend/dist"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8085
INQ_LOG = "/app/data/contact_inquiries.jsonl"

def sec_headers():
    return {
        "Content-Security-Policy": "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; connect-src 'self'",
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Cache-Control": "public, max-age=300",
    }

class NTrustHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DOCROOT, **kw)

    def _send(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in sec_headers().items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        p = urlparse(self.path).path
        if p == "/health":
            body = json.dumps({"status": "healthy", "service": "ntrust-web", "port": PORT}).encode()
            return self._send(200, "application/json", body)
        rel = unquote(p.lstrip("/"))
        if not rel or rel.endswith("/"):
            rel = rel + "index.html"
        fs = os.path.realpath(os.path.join(DOCROOT, rel))
        if not fs.startswith(os.path.realpath(DOCROOT)) or not os.path.isfile(fs):
            alt = os.path.join(DOCROOT, "404.html")
            if os.path.isfile(alt):
                with open(alt, "rb") as f:
                    return self._send(404, "text/html; charset=utf-8", f.read())
            return self._send(404, "text/plain; charset=utf-8", b"Not Found")
        ext = os.path.splitext(fs)[1].lower()
        ctype = "application/octet-stream"
        if ext == ".html": ctype = "text/html; charset=utf-8"
        elif ext == ".css": ctype = "text/css; charset=utf-8"
        elif ext == ".js":  ctype = "application/javascript; charset=utf-8"
        elif ext == ".svg": ctype = "image/svg+xml"
        elif ext == ".png": ctype = "image/png"
        elif ext == ".jpg" or ext == ".jpeg": ctype = "image/jpeg"
        elif ext == ".ico": ctype = "image/x-icon"
        elif ext == ".webp": ctype = "image/webp"
        elif ext == ".txt": ctype = "text/plain; charset=utf-8"
        elif ext == ".xml": ctype = "application/xml"
        elif ext == ".json": ctype = "application/json"
        elif ext == ".pdf": ctype = "application/pdf"
        elif ext == ".woff2": ctype = "font/woff2"
        elif ext == ".woff": ctype = "font/woff"
        with open(fs, "rb") as f:
            return self._send(200, ctype, f.read())

    def do_POST(self):
        p = urlparse(self.path).path
        if p != "/api/contact":
            return self._send(404, "application/json", b'{"ok": false, "error": "not_found"}')
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b""
            ctype = self.headers.get("Content-Type", "")
            if "application/json" in ctype:
                data = json.loads(raw.decode("utf-8", errors="replace"))
            else:
                from urllib.parse import parse_qs
                data = {k: v[0] for k, v in parse_qs(raw.decode("utf-8", errors="replace")).items()}
            name = str(data.get("name", "")).strip()[:120]
            email = str(data.get("email", "")).strip()[:200]
            msg = str(data.get("message", "")).strip()[:4000]
            if not name or not email or "@" not in email:
                return self._send(400, "application/json", b'{"ok": false, "error": "validation"}')
            inq_id = "inq_" + hashlib.sha256((email + str(time.time())).encode()).hexdigest()[:12]
            record = {"id": inq_id, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                      "name": name, "email": email, "message": msg, "source": "ntrust-web-8085", "status": "new"}
            os.makedirs(os.path.dirname(INQ_LOG), exist_ok=True)
            with open(INQ_LOG, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
            return self._send(200, "application/json", json.dumps({"ok": True, "id": inq_id}).encode())
        except Exception as e:
            return self._send(500, "application/json", json.dumps({"ok": False, "error": str(e)}).encode())

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), fmt % args))

def run():
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), NTrustHandler) as httpd:
        sys.stderr.write(f"nTrust web serving {DOCROOT} on 0.0.0.0:{PORT}\n")
        httpd.serve_forever()

if __name__ == "__main__":
    run()
