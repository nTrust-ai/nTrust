"""
nTrust Shield MVP - FastAPI Skeleton & Health Endpoint Implementation
TASK-93B0E7 | Workstream: @shield | Phase 1: Production Foundation
Target: Python 3.11+ runtime, /health (200 OK), /metrics (Prometheus), Security Headers
"""

import platform
import time
from datetime import datetime, timezone
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import structlog

# Initialize structured logging
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger("info"),
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
)
logger = structlog.get_logger()

app = FastAPI(
    title="nTrust Shield API",
    description="Automated Incident Response Automation Platform",
    version="0.1.0"
)

# Prometheus Metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint", "status"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "HTTP request latency in seconds")

@app.middleware("http")
async def process_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    REQUEST_LATENCY.observe(duration)
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()

    # Security Headers (NIST/AWS WAF baseline)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"

    return response

@app.get("/health")
async def health_check():
    """Health check endpoint returning 200 OK with system metadata."""
    logger.info("health_check", service="ntrust-shield-api", ts=datetime.now(timezone.utc).isoformat())
    return {
        "status": "healthy",
        "service": "ntrust-shield-api",
        "python_version": platform.python_version(),
        "uptime_seconds": time.time(),
        "compliance_baseline": "Phase 1 Infrastructure v1"
    }

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint."""
    return JSONResponse(
        content=generate_latest().decode("utf-8"),
        media_type=CONTENT_TYPE_LATEST
    )

@app.get("/")
async def root():
    return {"message": "nTrust Shield API initialized", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    # Run on 0.0.0.0:8000 for local Docker mapping
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
