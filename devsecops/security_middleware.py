"""
DevSecOps Security Baseline & Audit Logging Middleware
Task: TASK-90A174 | Owner: Sarah Martinez
Compliance: NIST AI RMF, EU AI Act HITL
"""

import time
import uuid
import logging
from typing import Dict, Any
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


class SecurityAuditMiddleware(BaseHTTPMiddleware):
    """Implements mandatory audit logging and security header enforcement."""

    def __init__(self, app: FastAPI, log_path: str = "/var/log/ntrust_audit.log"):
        super().__init__(app)
        self.logger = logging.getLogger("ntrust_security")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(log_path)
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(request_id)s | %(message)s"
            )
        )
        self.logger.addHandler(handler)

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        request_id = str(uuid.uuid4())

        # Enforce strict security headers
        response = await call_next(request)
        process_time = time.time() - start_time

        self.logger.info(
            f"Request: {request.method} {request.url.path} "
            f"| Status: {response.status_code} | Time: {process_time:.4f}s "
            f"| IP: {request.client.host}"
        )

        # Apply security headers per NIST/OWASP guidelines
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Strict-Transport-Security"] = (
            "max-age=31536000; includeSubDomains"
        )
        response.headers["Content-Security-Policy"] = "default-src 'self'"

        return response


def initialize_security_gates(app: FastAPI):
    """Registers security middleware and health endpoints."""
    app.add_middleware(SecurityAuditMiddleware, app=app)

    @app.get("/health")
    async def health_check():
        return {"status": "secure", "uptime": time.time(), "compliance": "NIST_RMF_V4"}
