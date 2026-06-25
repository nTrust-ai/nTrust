from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import logging
import sys

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/app/logs/app.log')
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="nTrust Shield MVP",
    description="AI-driven Incident Response Automation Platform",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration"""
    logger.info("Health check requested")
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "nTrust Shield MVP",
            "version": "0.1.0",
            "timestamp": "2026-06-24T21:40:37Z"
        },
        status_code=200
    )

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    logger.info("Metrics endpoint requested")
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/")
async def root():
    """Root endpoint"""
    logger.info("Root endpoint accessed")
    return JSONResponse(
        content={
            "service": "nTrust Shield MVP",
            "status": "running",
            "endpoints": {
                "health": "/health",
                "metrics": "/metrics"
            }
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)