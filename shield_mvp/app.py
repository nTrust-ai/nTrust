"""
nTrust Shield MVP Core API
Phase 1: Infrastructure & Product Launch
Target Environment: Cloud-native, Docker/Kubernetes
"""

import json
import os
import time
import logging
from logging.handlers import RotatingFileHandler
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import uuid

# --- Configuration & Logging Setup ---
LOG_DIR = "/app/logs"
LOG_FILE = f"{LOG_DIR}/shield_mvp.log"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("shield_mvp")

json_handler = RotatingFileHandler(LOG_FILE, maxBytes=10_485_760, backupCount=5)
json_handler.setFormatter(
    logging.Formatter(
        '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
    )
)
logger.addHandler(json_handler)

# --- Prometheus Metrics ---
TRIAGE_COUNTER = Counter("shield_triage_total", "Total alert triages processed")
CONTAIN_COUNTER = Counter("shield_contain_total", "Total containment actions executed")
REQUEST_LATENCY = Histogram("shield_request_latency_seconds", "Request latency")


# --- Pydantic Models ---
class AlertPayload(BaseModel):
    source_ip: str
    event_type: str  # e.g., "brute_force", "malware_detected"
    severity: int  # 1-10
    timestamp: str


class PlaybookAction(BaseModel):
    action_type: str  # e.g., "isolate_container", "block_ip", "update_fw_rule"
    target_id: str
    parameters: dict = {}


# --- Application Lifecycle ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("nTrust Shield MVP initializing...")
    yield
    logger.info("nTrust Shield MVP shutting down gracefully.")


app = FastAPI(title="nTrust Shield MVP", version="0.1.0", lifespan=lifespan)


# --- Middleware: Security Headers & Structured Logging ---
@app.middleware("http")
async def security_headers_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)

    # Enforce strict security headers
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )
    response.headers["Content-Security-Policy"] = "default-src 'self'"

    latency = time.time() - start_time
    logger.info(
        f"{request.method} {request.url.path} | Status: {response.status_code} | Latency: {latency:.3f}s"
    )
    return response


# --- Endpoints ---
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "nTrust Shield MVP",
        "uptime_start": time.time(),
    }


@app.get("/metrics")
async def prometheus_metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/api/v1/triage")
async def triage_alert(alert: AlertPayload):
    TRIAGE_COUNTER.inc()

    # Simulated ML Triage Logic
    priority = "low"
    if alert.severity >= 8:
        priority = "critical"
    elif alert.severity >= 5:
        priority = "high"

    logger.info(
        f"Triage executed for {alert.event_type} from {alert.source_ip}. Priority: {priority}"
    )

    return {
        "task_id": str(uuid.uuid4()),
        "status": "triaged",
        "assigned_priority": priority,
        "recommended_action": (
            "human_review" if priority == "critical" else "automated_logging"
        ),
    }


@app.post("/api/v1/contain")
async def execute_containment(playbook: PlaybookAction):
    CONTAIN_COUNTER.inc()

    # Simulated Containment Execution
    logger.info(
        f"Executing containment playbook: {playbook.action_type} on target {playbook.target_id}"
    )

    # In Phase 1, we simulate execution. Phase 2 will integrate with live infra.
    return {
        "execution_id": str(uuid.uuid4()),
        "status": "completed",
        "playbook_applied": playbook.action_type,
        "target_affected": playbook.target_id,
        "next_steps": "Verify isolation and update audit logs",
    }


# Fallback for unhandled routes
@app.get("/")
async def root():
    return {"message": "nTrust Shield MVP Core API is running.", "docs": "/docs"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
