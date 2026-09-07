"""
nTrust Shield MVP - FastAPI Skeleton & Security Baseline
Author: Product Strategist (Architect)
Date: 2026-06-24
Milestone: TASK-93B0E7 / TASK-9746DD Integration
"""

import sys
import os
import time
import logging
import json
from datetime import datetime, timezone
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from prometheus_client import CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST

# -----------------------------------------------------------------------------
# 1. ENVIRONMENT & RUNTIME VALIDATION (Python 3.11+ Mandate)
# -----------------------------------------------------------------------------
REQUIRED_PYTHON_VERSION = (3, 11)
CURRENT_PYTHON_VERSION = sys.version_info[:2]

if CURRENT_PYTHON_VERSION < REQUIRED_PYTHON_VERSION:
    raise RuntimeError(
        f"nTrust Shield requires Python {REQUIRED_PYTHON_VERSION[0]}.{REQUIRED_PYTHON_VERSION[1]}+. "
        f"Detected version: {'.'.join(map(str, CURRENT_PYTHON_VERSION))}"
    )

# -----------------------------------------------------------------------------
# 2. LOGGING & AUDIT MIDDLEWARE CONFIGURATION
# -----------------------------------------------------------------------------
LOG_DIR = "/app/data/orgs/org_ntrust/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "shield_audit.log")),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("ntrust.shield")


# -----------------------------------------------------------------------------
# 3. APPLICATION LIFECYCLE & HEALTH CHECKS
# -----------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing nTrust Shield MVP environment...")
    yield
    logger.info("Shutting down nTrust Shield MVP gracefully.")


app = FastAPI(
    title="nTrust Shield MVP",
    description="Automated Incident Response & Privacy Compliance Skeleton",
    version="0.1.0",
    lifespan=lifespan,
)


# -----------------------------------------------------------------------------
# 4. CORE ENDPOINTS
# -----------------------------------------------------------------------------
@app.get("/health")
async def health_check():
    """Standard Kubernetes/Docker health probe endpoint."""
    return {
        "status": "healthy",
        "service": "ntrust-shield-mvp",
        "python_version": f"{'.'.join(map(str, sys.version_info[:3]))}",
        "uptime_seconds": round(time.time() - app.state.start_time, 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/metrics")
async def metrics_endpoint():
    """Prometheus-compatible metrics endpoint."""
    return Response(
        content=generate_latest(CollectorRegistry()),
        media_type=CONTENT_TYPE_LATEST,
        headers={"X-Content-Type-Options": "nosniff"},
    )


# -----------------------------------------------------------------------------
# 5. SECURITY HEADERS & AUDIT MIDDLEWARE (TASK-9746DD)
# -----------------------------------------------------------------------------
class AuditSecurityMiddleware:
    """Enforces security headers, emits structured JSON audit logs."""

    REQUIRED_HEADERS = {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Content-Security-Policy": "default-src 'self'",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        start_time = time.time()

        await self.app(scope, receive, send)

        duration = time.time() - start_time
        request_id = f"req-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}-{int(duration*1000)}"

        # Emit structured JSON audit log
        audit_entry = {
            "event": "http_request",
            "request_id": request_id,
            "method": scope.get("method"),
            "path": scope.get("path"),
            "status_code": (
                scope.get("response_headers")[0][1]
                if scope.get("response_headers")
                else 200
            ),
            "duration_ms": round(duration * 1000, 2),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        logger.info(json.dumps(audit_entry))


app.add_middleware(AuditSecurityMiddleware)


# -----------------------------------------------------------------------------
# 6. ROOT & METADATA ENDPOINTS
# -----------------------------------------------------------------------------
@app.get("/")
async def root():
    return {
        "service": "nTrust Shield MVP",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
        "metrics": "/metrics",
    }


# -----------------------------------------------------------------------------
# 7. EXCEPTION HANDLER FOR COMPLIANCE & AUDIT TRACING
# -----------------------------------------------------------------------------
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception in {request.method} {request.url.path}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "request_id": "audit-traced"},
    )


if __name__ == "__main__":
    import uvicorn

    app.state.start_time = time.time()
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
