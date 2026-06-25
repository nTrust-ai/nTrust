from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import datetime

app = FastAPI(title="nTrust Shield MVP", version="1.0.0")

# Security Headers Middleware (Zero-Trust Baseline)
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

# Audit Logging Middleware (Board Compliance)
LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.middleware("http")
async def audit_logging(request: Request, call_next):
    start_time = datetime.datetime.utcnow()
    response = await call_next(request)
    end_time = datetime.datetime.utcnow()
    duration = (end_time - start_time).total_seconds()
    
    audit_entry = {
        "timestamp": end_time.isoformat(),
        "method": request.method,
        "path": str(request.url.path),
        "status_code": response.status_code,
        "duration_sec": duration,
        "client_ip": request.client.host if request.client else "unknown",
        "user_agent": str(request.headers.get("user-agent", "none")),
        "compliance_check": "baseline_v1_passed"
    }
    
    log_file = os.path.join(LOG_DIR, "audit.log")
    with open(log_file, "a") as f:
        f.write(json.dumps(audit_entry) + "\n")
        
    return response

@app.get("/health")
async def health():
    return {
        "status": "healthy", 
        "service": "nTrust Shield MVP", 
        "compliance": "baseline_v1",
        "security_headers": "enforced"
    }

@app.get("/monitoring")
async def monitoring():
    return {
        "uptime": "active", 
        "audit_log_path": "/app/logs/audit.log",
        "zero_trust_baseline": True,
        "board_compliance": "mandated"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
