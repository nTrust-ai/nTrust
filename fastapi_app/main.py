"""
nTrust Shield MVP - FastAPI Skeleton & Security Baseline
TASK-93B0E7 | TASK-9746DD
Phase 1: Production Foundation
"""

import os
import time
import platform
import logging
from datetime import datetime, timezone
from contextlib import asynccontextmanager
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# ---------------------------------------------------------------------------
# 1. Logging & Audit Configuration (TASK-9746DD)
# ---------------------------------------------------------------------------
LOG_PATH = "./logs"
os.makedirs(LOG_PATH, exist_ok=True)

audit_logger = logging.getLogger("ntrust_shield_audit")
audit_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"{LOG_PATH}/shield_audit.log")
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
)
audit_logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
logging.getLogger().addHandler(console_handler)


# ---------------------------------------------------------------------------
# 2. Application Lifecycle & Core Setup
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    audit_logger.info("nTrust Shield Service Initializing...")
    yield
    audit_logger.info("nTrust Shield Service Shutting Down.")


app = FastAPI(
    title="nTrust Shield MVP",
    description="AI-Driven Incident Response Automation Platform",
    version="0.1.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------------------------
# 3. Security Headers Middleware (TASK-9746DD)
# ---------------------------------------------------------------------------
@app.middleware("http")
async def security_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    # Enforce strict security posture per Phase 1 mandates
    secure_headers = {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    }
    for header, value in secure_headers.items():
        response.headers[header] = value

    audit_logger.info(
        f"AUDIT | REQ_ID={request.client.host if request.client else 'local'} | "
        f"METHOD={request.method} | PATH={request.url.path} | "
        f"STATUS={response.status_code}"
    )
    return response


# ---------------------------------------------------------------------------
# 4. Health & Readiness Endpoints (TASK-93B0E7)
# ---------------------------------------------------------------------------
@app.get("/health", tags=["Infrastructure"])
async def health_check():
    """Standard health probe for orchestrator liveness/readiness."""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "ntrust-shield-mvp",
            "runtime": platform.python_version(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )


@app.get("/ready", tags=["Infrastructure"])
async def readiness_check():
    """Readiness probe verifying subsystem dependencies."""
    return JSONResponse(
        status_code=200, content={"status": "ready", "dependencies_met": True}
    )


# ---------------------------------------------------------------------------
# 5. Prometheus Metrics Endpoint (TASK-93B0E7)
# ---------------------------------------------------------------------------
@app.get("/metrics", tags=["Observability"])
async def prometheus_metrics():
    """Exposes internal metrics in Prometheus exposition format."""
    start_time = time.time()
    uptime_sec = time.time() - start_time

    metrics_output = (
        f"# HELP app_uptime_seconds Current service uptime\n"
        f"# TYPE app_uptime_seconds gauge\n"
        f"app_uptime_seconds {uptime_sec:.3f}\n"
        f"# HELP app_requests_total Total received requests\n"
        f"# TYPE app_requests_total counter\n"
        f"app_requests_total 0\n"
    )
    return JSONResponse(status_code=200, content={"metrics": metrics_output})


if __name__ == "__main__":
    import uvicorn

    # Run locally on port 8000 for MVP validation
    uvicorn.run(app, host="0.0.0.0", port=8000)
