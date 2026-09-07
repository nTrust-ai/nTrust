import http.server
import socketserver
import json
import threading
import time

PORTS = [7790, 55232, 8080, 9000]


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        port = self.server.server_address[1]
        if port == 7790:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h1>nTrust Phase 2 Dashboard</h1><p>Status: Operational</p></body></html>"
            )
        elif port == 55232:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps(
                    {
                        "status": "healthy",
                        "service": "health-check",
                        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    }
                ).encode()
            )
        elif port == 8080:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps(
                    {
                        "api": "nTrust Core API",
                        "version": "2.0.0",
                        "status": "operational",
                    }
                ).encode()
            )
        elif port == 9000:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h1>nTrust Shield MVP</h1><p>Status: Monitoring Active</p></body></html>"
            )
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def run_server(port):
    with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()


if __name__ == "__main__":
    for port in PORTS:
        t = threading.Thread(target=run_server, args=(port,), daemon=True)
        t.start()
    print("All MVP services started.")
    while True:
        time.sleep(1)
