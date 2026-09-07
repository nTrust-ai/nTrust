#!/usr/bin/env python3
"""nTrust.ai Corporate Site Server (Port 8085)

Serves the Board-approved static multi-page corporate site (docroot arg) and:
  GET  /healthz      -> {"status":"healthy","service":"ntrust-corporate-site","port":8085,...}
  POST /api/contact  -> persists inquiry JSONL, returns {"ok":true,"id":"inq_<hex>",...}
  GET  * (static)    -> SimpleHTTPRequestHandler over docroot
  404 fallback       -> serves docroot/404.html with HTTP 404 (Cloudflare Pages parity)

Usage: python3 ntrust_web_server.py [docroot] [port]
EU AI Act / NIST AI RMF traceability: inquiries appended to JSONL audit store
(org_ntrust/api/contact_inquiries.jsonl) with UTC timestamp + source IP.
Binds 0.0.0.0 explicitly (Localhost Bind Trap compliance).
"""

import http.server
import json
import os
import secrets
import sys
import time
from datetime import datetime, timezone
from urllib.parse import urlparse, parse_qs

PORT = int(
    sys.argv[2] if len(sys.argv) > 2 else os.environ.get("CORP_SITE_PORT", "8085")
)
DOCROOT = (
    sys.argv[1]
    if len(sys.argv) > 1
    else os.environ.get("CORP_SITE_DOCROOT", "/app/data/frontend/dist")
)
INBOX_PRIMARY = os.environ.get(
    "CORP_INBOX_PRIMARY", "/app/data/orgs/org_ntrust/api/contact_inquiries.jsonl"
)
INBOX_FALLBACK = os.environ.get(
    "CORP_INBOX_FALLBACK", "/app/data/frontend/data/contact_inquiries.jsonl"
)
ALLOWED_FIELDS = ("name", "email", "company", "subject", "message")


class CorporateSiteHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DOCROOT, **kwargs)

    def _send_json(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _persist_inquiry(self, record):
        line = json.dumps(record, ensure_ascii=False) + "\n"
        for path in (INBOX_PRIMARY, INBOX_FALLBACK):
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "a", encoding="utf-8") as fh:
                    fh.write(line)
                return path
            except OSError:
                continue
        return None

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/healthz":
            self._send_json(
                200,
                {
                    "status": "healthy",
                    "service": "ntrust-corporate-site",
                    "port": PORT,
                    "compliance_framework": "NIST AI RMF / EU AI Act",
                    "utc": datetime.now(timezone.utc).isoformat(),
                },
            )
            return
        if parsed.path == "/api/contact":
            self._send_json(
                200,
                {
                    "ok": True,
                    "endpoint": "api/contact",
                    "method": "GET",
                    "hint": "use POST",
                },
            )
            return
        try:
            super().do_GET()
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != "/api/contact":
            self.send_error(404, "Not Found")
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length).decode("utf-8", "ignore")
        except Exception:
            raw = ""
        data = {}
        try:
            data = {k: (v[0] if v else "") for k, v in parse_qs(raw).items()}
        except Exception:
            pass
        if not data:
            try:
                data = json.loads(raw or "{}")
            except Exception:
                data = {}
        cleaned = {k: str(data.get(k, "")).strip()[:2000] for k in ALLOWED_FIELDS}
        if not cleaned.get("email") or "@" not in cleaned["email"]:
            self._send_json(400, {"ok": False, "error": "valid email required"})
            return
        inquiry_id = "inq_" + secrets.token_hex(6)
        record = {
            "id": inquiry_id,
            "ts": datetime.now(timezone.utc).isoformat(),
            "source_ip": self.client_address[0] if self.client_address else "unknown",
            "ua": (self.headers.get("User-Agent") or "")[:300],
            "data": cleaned,
        }
        stored = self._persist_inquiry(record)
        if stored is None:
            self._send_json(500, {"ok": False, "error": "persistence unavailable"})
            return
        self._send_json(200, {"ok": True, "id": inquiry_id, "stored": stored})

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            try:
                with open(os.path.join(DOCROOT, "404.html"), "rb") as fh:
                    body = fh.read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            except OSError:
                pass
        super().send_error(code, message, explain)

    def log_message(self, fmt, *args):
        sys.stderr.write(
            "[corp-8085] %s %s\n" % (self.log_date_time_string(), fmt % args)
        )


def run():
    os.makedirs(os.path.dirname(INBOX_PRIMARY), exist_ok=True)
    with http.server.ThreadingHTTPServer(
        ("0.0.0.0", PORT), CorporateSiteHandler
    ) as httpd:
        sys.stderr.write("[corp-8085] serving %s on 0.0.0.0:%d\n" % (DOCROOT, PORT))
        httpd.serve_forever()


if __name__ == "__main__":
    run()
