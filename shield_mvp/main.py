from fastapi import FastAPI, Request
import logging
import time

app = FastAPI(title="nTrust Shield MVP", version="0.1.0")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("shield_mvp_audit")


@app.middleware("http")
async def audit_logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(
        f"AUDIT | method={request.method} path={request.url.path} "
        f"status={response.status_code} duration={duration:.3f}s ip={request.client.host}"
    )
    return response


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "shield_mvp",
        "compliance": "phase1_baseline",
    }


@app.get("/monitoring/metrics")
def system_metrics():
    return {
        "uptime_seconds": time.time(),
        "audit_log_path": "/app/logs/shield_audit.log",
        "security_headers": ["X-Frame-Options", "HSTS", "CSP"],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
