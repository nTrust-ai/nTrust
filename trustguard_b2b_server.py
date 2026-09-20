"""
nTrust.ai — TrustGuard B2B Pricing & Commercialization Service
Port 55005: Enterprise Cybersecurity API Gateway

Phase 3 Revenue Launch | NIST AI RMF Compliant
Replaces directory listing with proper JSON API responses.
"""
import http.server
import json
import socketserver
from datetime import datetime

PORT = 55005

class TrustGuardHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.end_headers()
            self.wfile.write(json.dumps({
                 "service": "TrustGuard B2B Pricing Service",
                 "status": "operational",
                 "version": "3.0.0",
                 "timestamp": datetime.utcnow().isoformat(),
                 "compliance": "NIST AI RMF / EU AI Act",
                 "endpoints": {
                     "health": "/health",
                     "pricing": "/pricing",
                     "tiers": "/tiers"
                 }
             }).encode())
        elif self.path == "/pricing":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                 "plans": [
                     {"tier": "Starter", "price_usd": 99, "features": ["Basic AI Analysis", "Email Support"]},
                     {"tier": "Professional", "price_usd": 499, "features": ["Advanced AI Analysis", "Priority Support", "Compliance Reports"]},
                     {"tier": "Enterprise", "price_usd": 1999, "features": ["Full Suite", "Dedicated Engineer", "SLA Guarantee"]}
                 ]
             }).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), TrustGuardHandler) as httpd:
        print(f"TrustGuard B2B Service running on port {PORT}")
        httpd.serve_forever()
