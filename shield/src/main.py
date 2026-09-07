"""
nTrust Shield MVP - Core Application
Phase 1: Production Foundation
Workstream: @shield
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.middleware.base import BaseHTTPMiddleware
import json
import time
import logging
import os

# Configure Logging for Audit Trail
os.makedirs("/app/data/orgs/org_ntrust/logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/app/data/orgs/org_ntrust/logs/audit.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("ntrust_shield")

app = FastAPI(
    title="nTrust Shield MVP",
    description="Automated intelligence and cybersecurity service layer.",
    version="0.1.0",
)


# Security Headers Middleware
class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = (
            "max-age=31536000; includeSubDomains"
        )
        return response


app.add_middleware(SecurityHeadersMiddleware)


# Health Check Endpoint
@app.get("/health")
async def health_check():
    """
    Liveness probe for orchestration.
    Returns 200 OK if the service is running.
    """
    logger.info("Health check requested")
    return JSONResponse(
        content={"status": "healthy", "service": "ntrust-shield", "version": "0.1.0"}
    )


# Metrics Endpoint (Prometheus format placeholder)
@app.get("/metrics")
async def metrics():
    """
    Exposes Prometheus-compatible metrics.
    """
    logger.info("Metrics requested")
    metrics_data = f"""# HELP ntrust_shield_requests_total Total requests
# TYPE ntrust_shield_requests_total counter
ntrust_shield_requests_total 1
# HELP ntrust_shield_uptime_seconds Uptime in seconds
# TYPE ntrust_shield_uptime_seconds gauge
ntrust_shield_uptime_seconds {time.time()}
"""
    return PlainTextResponse(content=metrics_data, media_type="text/plain")


# Root Endpoint
@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "nTrust Shield MVP - Operational", "status": "active"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
