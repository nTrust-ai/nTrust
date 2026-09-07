#!/usr/bin/env python3
"""nTrust Catalog Service - Port 9090"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os


class CatalogHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"healthy","service":"ntrust-catalog"}')
        elif self.path.startswith("/api/"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"service": "ntrust-catalog", "path": self.path}
            self.wfile.write(str(response).encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """<html><head><title>nTrust Catalog</title></head>
                        <body>
                            <h1>nTrust Catalog Service (Port 9090)</h1>
                            <p>Service Status: HEALTHY</p>
                        </body></html>"""
            self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        response = {"status": "success", "received": len(post_data)}
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(str(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 9090), CatalogHandler)
    print(f"nTrust Catalog Service listening on port 9090...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()
