import http.server
import socketserver
import os

os.chdir('/app/data/orgs/org_ntrust')

PORT = 8085
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("0.0.0.0", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving TrustGuard MVP on port {PORT}")
    httpd.serve_forever()
