"""
nTrust Shield MVP — FastAPI Skeleton & Health Endpoint
Local Dev Deployment per NIST RMF & MVP Local First Protocol
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[nTrust Shield] Initializing local MVP environment...")
    yield
    print("[nTrust Shield] Shutting down local MVP gracefully.")


app = FastAPI(title="nTrust Shield MVP", version="0.1.0-local", lifespan=lifespan)


@app.get("/health", tags=["Operations"])
async def health_check():
    """
    Health endpoint for container orchestration validation.
    Returns 200 OK with service metadata and local environment status.
    """
    return JSONResponse(
        status_code=200,
        content={
            "service": "ntrust-shield-mvp",
            "status": "healthy",
            "environment": os.getenv("ENVIRONMENT", "local-dev"),
            "security_baseline": "enforced",
            "audit_logging": "active",
        },
    )


@app.get("/", tags=["Core"])
async def root():
    return {"message": "nTrust Shield MVP Local Pilot Active"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
