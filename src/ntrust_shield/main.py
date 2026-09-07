"""
nTrust Shield MVP — FastAPI Skeleton & Security Baseline
Workstream: @shield | Phase: 1 (Production Foundation)
Target Env: python:3.11-slim / Cloud-Native Microservices
"""

import sys
import time
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

# ─── Runtime Verification & Config ───────────────────────────────────────────────
assert sys.version_info >= (3, 11), "nTrust Shield requires Python 3.11+ baseline."

app = FastAPI(
    title="nTrust Shield",
    version="0.1.0-mvp",
    description="AI-driven Incident Response Automation Platform",
)

# Structured JSON Logger (Audit Baseline)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("ntrust_shield")


# ─── Middleware: Security Headers & Audit Logging ────────────────────────────────
@app.middleware("http")
async def security_audit_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    # Enforce Phase 1 Infrastructure Baseline (SOP Compliance Checklist v1)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = (
        "max-age=63072000; includeSubDomains"
    )
    response.headers["Cache-Control"] = "no-store"

    # Audit Logging Structure (JSON-ready for future /app/logs ingestion)
    latency = time.time() - start_time
    logger.info(
        f"AUDIT: {request.method} {request.url.path} | "
        f"Status: {response.status_code} | Latency: {latency:.3f}s | Client: {request.client.host}"
    )

    return response


# ─── Health & Observability Endpoints ────────────────────────────────────────────
@app.get("/health", tags=["Infrastructure"])
async def health_check():
    """Returns 200 OK with service metadata and Python runtime verification."""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "ntrust-shield",
            "phase": "1-infrastructure",
            "python_version": sys.version.split()[0],
            "uptime_seconds": time.time(),
            "compliance": "SOP-Infra-Baseline-v1",
        },
    )


@app.get("/metrics", tags=["Observability"])
async def metrics_endpoint():
    """Prometheus-compatible metrics output for container orchestration."""
    uptime = time.time()
    metrics_data = f"""# HELP ntrust_shield_uptime_seconds Service uptime in seconds.
# TYPE ntrust_shield_uptime_seconds gauge
ntrust_shield_uptime_seconds {uptime}
# HELP ntrust_shield_requests_total Total requests handled.
# TYPE ntrust_shield_requests_total counter
ntrust_shield_requests_total 0
"""
    return Response(content=metrics_data, media_type="text/plain; version=0.0.4")


# ─── Root & Default Routing ─────────────────────────────────────────────────────
@app.get("/", tags=["Root"])
async def root():
    return JSONResponse(
        status_code=200,
        content={"message": "nTrust Shield API v0.1.0 active", "docs": "/redoc"},
    )


if __name__ == "__main__":
    import uvicorn

    logger.info("Initializing nTrust Shield FastAPI server on 0.0.0.0:8080...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
