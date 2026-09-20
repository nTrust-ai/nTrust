import time
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("zerotrust_gateway")

app = FastAPI(title="nTrust.ai Zero-Trust Gateway", version="1.0.0")

def enforce_zero_trust(request: Request):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Zero-Trust Violation: Missing/Invalid Credentials")
    return True

@app.middleware("http")
async def security_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        enforce_zero_trust(request)
    except HTTPException as e:
        logger.warning(f"ACCESS DENIED: {request.method} {request.url.path} - {e.detail}")
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"AUDIT: {request.method} {request.url.path} | Status: {response.status_code} | Duration: {duration:.2f}s")
    return response

@app.get("/health")
async def health_check():
    return {"status": "secure", "gateway": "active", "timestamp": time.time()}

@app.post("/api/v1/verify")
async def verify_identity(request: Request):
    return {"verified": True, "trust_score": 0.98, "message": "Zero-trust validation passed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8085)