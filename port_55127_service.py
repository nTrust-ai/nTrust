#!/usr/bin/env python3
"""
nTrust.ai Port 55127 Service Restoration Script
Phase 3 Revenue Operations Critical Infrastructure

This script implements a lightweight HTTP service on port 55127
that serves the Phase 3 revenue MVP endpoints.
"""

import http.server
import socketserver
import json
import os
from datetime import datetime

PORT = 55127
BIND_ADDRESS = "0.0.0.0"   # Critical: Bind to all interfaces for external access

class RevenueMVPHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
             "status": "operational",
             "service": "nTrust.ai Phase 3 Revenue MVP",
             "port": PORT,
             "timestamp": datetime.utcnow().isoformat(),
             "endpoints": [
                 "/health",
                 "/products",
                 "/pricing",
                 "/contact"
             ]
         }
        
        if self.path == '/health':
            response["health_check"] = "passing"
            response["uptime"] = "active"
        elif self.path == '/products':
            response["products"] = [
                 {"id": 1, "name": "TrustGuard", "status": "live"},
                 {"id": 2, "name": "AppSec Platform", "status": "coming_soon"}
             ]
        elif self.path == '/pricing':
            response["pricing"] = [
                 {"tier": "Foundation", "price": "$499/mo"},
                 {"tier": "Professional", "price": "$1,499/mo"},
                 {"tier": "Enterprise", "price": "Custom"}
             ]
            
        self.wfile.write(json.dumps(response, indent=2).encode())
    
    def log_message(self, format, *args):
         # Suppress default logging to reduce noise
        pass

def serve_forever():
    with socketserver.TCPServer((BIND_ADDRESS, PORT), RevenueMVPHandler) as httpd:
        print(f"✅ nTrust.ai Port {PORT} Service Running on {BIND_ADDRESS}")
        print(f"   Health Check: http://{BIND_ADDRESS}:{PORT}/health")
        print(f"   Products API: http://{BIND_ADDRESS}:{PORT}/products")
        httpd.serve_forever()

if __name__ == "__main__":
    serve_forever()
