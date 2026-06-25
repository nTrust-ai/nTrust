from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {
             "status": "healthy",
             "service": "ntrust-mvp-localhost",
             "phase": 1,
             "timestamp": "2026-06-24T10:55:00Z"
         }
        self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), HealthHandler)
    print("✅ MVP Localhost Service Active on Port 8000")
    server.serve_forever()