"""
nTrust Shield MVP - Main Application Entry Point
Workstream: @shield | Phase: 1 (Production Foundation)
Date: 2026-06-24
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
import psutil
import os

app = FastAPI(
    title="nTrust Shield MVP",
    description="Automated intelligence and cybersecurity service platform",
    version="0.1.0"
)

# Security Headers Middleware
class SecurityHeadersMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            async def send_wrapper(message):
                if message["type"] == "http.response.start":
                    headers = list(message.get("headers", []))
                    headers.append((b"X-Content-Type-Options", b"nosniff"))
                    headers.append((b"X-Frame-Options", b"DENY"))
                    headers.append((b"X-XSS-Protection", b"1; mode=block"))
                    headers.append((b"Strict-Transport-Security", b"max-age=31536000; includeSubDomains"))
                    message["headers"] = headers
                await send(message)
            await self.app(scope, receive, send_wrapper)
        else:
            await self.app(scope, receive, send)

app.add_middleware(SecurityHeadersMiddleware)

# CORS Configuration (Restricted for MVP)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Local dev only
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Audit Logging Middleware
@app.middleware("http")
async def audit_logging(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    # Structured JSON log format
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "process_time_ms": round(process_time * 1000, 2),
        "client_host": request.client.host if request.client else "unknown",
        "user_agent": request.headers.get("user-agent", "unknown")
    }
    
    # In MVP, log to stdout (will be redirected to file in Docker)
    import logging
    logging.info(f"ACCESS_LOG: {log_entry}")
    
    return response

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint for Kubernetes/Load Balancer probes.
    Returns 200 OK if the service is running.
    """
    return {
        "status": "healthy",
        "service": "nTrust Shield MVP",
        "version": "0.1.0",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

@app.get("/metrics", tags=["Metrics"])
async def get_metrics():
    """
    Prometheus-style metrics endpoint.
    Returns system and application metrics in text format.
    """
    cpu_percent = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    metrics_text = f"""# HELP ntrust_cpu_percent CPU usage percentage
# TYPE ntrust_cpu_percent gauge
ntrust_cpu_percent {cpu_percent}

# HELP ntrust_memory_percent Memory usage percentage
# TYPE ntrust_memory_percent gauge
ntrust_memory_percent {memory.percent}

# HELP ntrust_disk_percent Disk usage percentage
# TYPE ntrust_disk_percent gauge
ntrust_disk_percent {disk.percent}

# HELP ntrust_uptime_seconds Service uptime in seconds
# TYPE ntrust_uptime_seconds counter
ntrust_uptime_seconds {time.time() - start_time}
"""
    return JSONResponse(content=metrics_text, media_type="text/plain")

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint returning service information."""
    return {
        "service": "nTrust Shield",
        "tagline": "It is the numbers we trust.",
        "status": "operational",
        "phase": "1 (Production Foundation)",
        "endpoints": ["/health", "/metrics"]
    }

# Startup event to log initialization
start_time = time.time()

@app.on_event("startup")
async def startup_event():
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("nTrust Shield MVP started successfully.")
    logging.info(f"Python version: {os.sys.version}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)