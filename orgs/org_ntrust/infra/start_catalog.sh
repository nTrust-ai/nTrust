#!/bin/bash
# Start Service Catalog on port 9090 with SO_REUSEADDR and timeout
cat > /tmp/catalog_server.py << 'PYEOF'
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json, time

class ReuseAddrHTTPServer(HTTPServer):
    allow_reuse_address = True
    
start_time = time.time()

class CatalogHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/health', '/api/health']:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'healthy'}).encode())
        elif self.path in ['/', '/index', '/catalog']:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            catalog = {'service': 'nTrust.ai Service Catalog', 'products': [{'id': 'PROD-DCCCF5', 'name': 'nTrust Shield'}, {'id': 'PROD-SUN001', 'name': 'SUN-Token NFC Security'}]}
            self.wfile.write(json.dumps(catalog).encode())

server = ReuseAddrHTTPServer(('0.0.0.0', 9090), CatalogHandler)
print(f"🚀 Service Catalog running on http://0.0.0.0:9090", flush=True)
server.serve_forever()
PYEOF

python /tmp/catalog_server.py &
sleep 2
curl -s http://localhost:9090/health && echo " ✅ Service Catalog restored!" || echo " ❌ Server failed to start"
