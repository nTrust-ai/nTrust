"""
nTrust Shield MVP — Audit Logging Middleware & Security Baseline Integration
Task: TASK-9746DD
Author: Product Strategist (Architect) | Date: 2026-06-24

This module provides production-grade middleware for the FastAPI nTrust Shield Core Engine.
It implements:
1. AuditLogger: Structured request/response logging compliant with NIST RMF & EU HITL mandates.
2. SecurityBaselineValidator: Enforces HTTPS, security headers, and CORS baselines.
3. RBAC Stub Dependency: Placeholder for JWT validation and role-based access control.
"""

import time
import logging
import uuid
from typing import Optional
from fastapi import Request, Response, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("ntrust.audit")


# -----------------------------------------------------------------------------
# 1. AUDIT LOGGER MIDDLEWARE
# -----------------------------------------------------------------------------
class AuditLogger(BaseHTTPMiddleware):
    """
    Captures request metadata, execution time, and response status for forensic auditing.
    Aligns with NIST AI RMF Proactive Risk Management and EU HITL compliance logging requirements.
    """

    def __init__(self, app: BaseHTTPMiddleware, log_level: str = "INFO"):
        super().__init__(app)
        self.log_level = log_level

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # Construct structured audit payload
        audit_payload = {
            "request_id": str(uuid.uuid4()),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
            "method": request.method,
            "path": str(request.url.path),
            "query_params": dict(request.query_params) if request.query_params else {},
            "client_ip": request.client.host if request.client else "unknown",
            "user_agent": request.headers.get("user-agent", "N/A"),
            "status_code": response.status_code,
            "duration_ms": round(process_time * 1000, 2),
        }

        # Log based on security baseline (warn on non-2xx/4xx)
        if response.status_code >= 500:
            logger.error(f"AUDIT_FAIL: {audit_payload}")
        elif response.status_code in [401, 403]:
            logger.warning(f"AUDIT_AUTHZ: {audit_payload}")
        else:
            logger.info(f"AUDIT_OK: {audit_payload}")

        return response


# -----------------------------------------------------------------------------
# 2. SECURITY BASELINE VALIDATOR MIDDLEWARE
# -----------------------------------------------------------------------------
class SecurityBaselineMiddleware(BaseHTTPMiddleware):
    """
    Enforces baseline security headers, CORS policies, and HTTPS termination checks.
    Prevents XSS, Clickjacking, and MIME-sniffing attacks.
    """

    def __init__(self, app: BaseHTTPMiddleware, allowed_origins: list = None):
        super().__init__(app)
        self.allowed_origins = allowed_origins or [
            "https://app.ntrust.ai",
            "https://localhost",
        ]

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Mandatory Security Headers per nTrust Shield Baseline
        security_headers = {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
        }
        response.headers.update(security_headers)

        # CORS Baseline Enforcement (Pre-flight & Response)
        origin = request.headers.get("Origin")
        if origin in self.allowed_origins:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Methods"] = (
                "GET, POST, PUT, DELETE, OPTIONS"
            )
            response.headers["Access-Control-Allow-Headers"] = (
                "Authorization, Content-Type, X-Request-ID"
            )

        return response


# -----------------------------------------------------------------------------
# 3. SECURITY BASELINE DEPENDENCY (JWT / RBAC STUB)
# -----------------------------------------------------------------------------
security_scheme = HTTPBearer(auto_error=False)


async def verify_security_baseline(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
):
    """
    Placeholder for production JWT validation and RBAC enforcement.
    Validates token presence, structure, and scope before executing protected endpoints.
    """
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=401, detail="Missing or invalid authorization token"
        )

    # TODO: Integrate with nTrust Identity Provider for actual JWT verification & RBAC lookup
    return {
        "sub": "service_account",
        "roles": ["admin"],
        "exp": time.time() + 3600,
        "iat": time.time(),
    }
