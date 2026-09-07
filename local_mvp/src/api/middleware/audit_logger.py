"""
nTrust Shield MVP — Audit Logging Middleware & Security Baseline
Implements structured request/response logging per NIST RMF requirements.
"""

import time
import json
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("ntrust-audit")
handler = logging.FileHandler("/app/logs/audit.log")
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class AuditLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        logger.info(
            f"AUDIT | Method={request.method} Path={request.url.path} "
            f"Status={response.status_code} Duration={process_time:.4f}s "
            f"ClientIP={request.client.host}"
        )

        return response
