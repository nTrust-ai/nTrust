from fastapi import FastAPI
from fastapi.responses import JSONResponse
import time
import os

app = FastAPI(
    title="nTrust Shield API",
    description="nTrust Shield MVP - Phase 1 Infrastructure",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration."""
    return JSONResponse({
        "status": "healthy",
        "timestamp": time.time(),
        "service": "ntrust-shield-api",
        "version": "0.1.0",
        "python_version": os.popen("python --version").read().strip()
    })

@app.get("/metrics")
async def metrics():
    """Prometheus-format metrics endpoint."""
    return JSONResponse({
        "metrics": {
            "ntrust_shield_requests_total": 1,
            "ntrust_shield_health_checks": 1,
            "ntrust_shield_uptime_seconds": 0
        },
        "format": "prometheus"
    })

@app.get("/")
async def root():
    """Root endpoint."""
    return JSONResponse({
        "service": "nTrust Shield API",
        "status": "active",
        "version": "0.1.0",
        "endpoints": ["/health", "/metrics"]
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)