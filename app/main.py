"""
nTrust Shield MVP — FastAPI Skeleton & Audit Logging Middleware
Phase 1 Pivot Execution | Local Sandbox Deployment
Author: Alex Chen, Lead Security Architect
Date: 2026-06-24
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import logging
import uuid
from datetime import datetime

# Configure secure audit logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
audit_logger = logging.getLogger('ntrust.audit')

app = FastAPI(
    title="nTrust Shield MVP",
    description="Core security & privacy service skeleton for local pilot testing.",
    version="0.1.0-local"
)

# Security Headers Middleware (NIST RMF / EU AI Act Compliance Baseline)
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

# Audit Logging Middleware
@app.middleware("http")
async def audit_logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = datetime.utcnow()

    # Log incoming request
    audit_logger.info(f"INBOUND | ID:{request_id} | {request.method} {request.url.path}")

    try:
        response = await call_next(request)
        audit_logger.info(f"OUTBOUND | ID:{request_id} | Status:{response.status_code} | Latency:{(datetime.utcnow() - start_time).total_seconds()}s")
        return response
    except Exception as e:
        audit_logger.error(f"ERROR | ID:{request_id} | {str(e)}")
        raise

@app.get("/health", tags=["System"])
async def health_check():
    """Public health endpoint for local pilot readiness validation."""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "nTrust Shield MVP",
            "environment": "local-sandbox",
            "timestamp": datetime.utcnow().isoformat(),
            "compliance_mode": "NIST-RMF / HITL-Compliant"
        }
    )

@app.get("/", tags=["Root"])
async def root():
    return {"message": "nTrust Shield MVP Local Pilot Active. Proceeding to Phase 2 Traction & Trust."}
