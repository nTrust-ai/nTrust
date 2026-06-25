"""
nTrust Shield MVP - FastAPI Skeleton & Security Baseline
Phase 1: Production Foundation | Workstream: @shield
Target Env: Python 3.11+ | python:3.11-slim base image compliant
"""

import logging
import sys
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Dict

from fastapi import FastAPI, Request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import uvicorn

# --------------------------------------------------------------------------- #
# 🛡️ Structured Audit Logging Setup (NIST RMF / EU AI Act HITL Compliance)
# --------------------------------------------------------------------------- #
class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
             "timestamp": datetime.now(timezone.utc).isoformat(),
             "level": record.levelname,
             "message": record.getMessage(),
             "module": record.module,
             "function": record.funcName,
             "line": record.lineno,
         }
        return super().format(str(log_data))

audit_logger = logging.getLogger("ntrust.shield.audit")
audit_logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
audit_logger.addHandler(handler)

# --------------------------------------------------------------------------- #
# 📊 Prometheus Metrics Setup
# --------------------------------------------------------------------------- #
REQUEST_COUNT = Counter("ntrust_shield_requests_total", "Total requests to nTrust Shield")
REQUEST_LATENCY = Histogram("ntrust_shield_request_latency_seconds", "Request latency in seconds")

# --------------------------------------------------------------------------- #
# 🧠 Application Lifecycle & State Management
# --------------------------------------------------------------------------- #
@asynccontextmanager
async def lifespan(app: FastAPI):
    audit_logger.info("🚀 nTrust Shield MVP initializing...")
    yield
    audit_logger.info("🛑 nTrust Shield MVP shutting down gracefully.")

app = FastAPI(
    title="nTrust Shield MVP",
    description="AI-driven Incident Response Automation Platform (MVP)",
    version="0.1.0",
    lifespan=lifespan
)

# --------------------------------------------------------------------------- #
# 🛡️ Security & Compliance Middleware
# --------------------------------------------------------------------------- #
@app.middleware("http")
async def security_headers_middleware(request: Request, call_next):
    response: Response = await call_next(request)
     # Enforce strict security headers per SOP compliance checklist
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

@app.middleware("http")
async def audit_and_metrics_middleware(request: Request, call_next):
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        response = await call_next(request)
    audit_logger.info(
        f"Incoming request: {request.method} {request.url.path}",
         extra={"extra_data": {"client_ip": request.client.host if request.client else "unknown"}}
     )
    return response

# --------------------------------------------------------------------------- #
# 🩺 Health & Readiness Endpoints
# --------------------------------------------------------------------------- #
@app.get("/health")
async def health_check():
    return {
         "status": "healthy",
         "service": "ntrust-shield-mvp",
         "version": "0.1.0",
         "uptime_since": datetime.now(timezone.utc).isoformat(),
         "compliance_framework": "NIST AI RMF / EU AI Act HITL Baseline"
     }

@app.get("/ready")
async def readiness_check():
     # Simulate dependency checks (DB, Cache, etc.) for Phase 1 foundation
    return {"status": "ready", "dependencies_met": True}

# --------------------------------------------------------------------------- #
# 📈 Metrics Endpoint (Prometheus Format)
# --------------------------------------------------------------------------- #
@app.get("/metrics")
async def metrics_endpoint():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
         headers={"Content-Type": CONTENT_TYPE_LATEST}
     )

# --------------------------------------------------------------------------- #
# 🚀 Entry Point (Run via: uvicorn main:app --host 0.0.0.0 --port 8000)
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
