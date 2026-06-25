"""nTrust Shield MVP Core API — FastAPI Skeleton & Audit Logging"""
import time
from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="nTrust Shield MVP", version="0.1.0-staging")

# Prometheus Metrics Registry
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

@app.middleware("http")
async def audit_and_track_metrics(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    REQUEST_LATENCY.observe(duration)
    return response

@app.get("/health")
async def health_check():
    return {
         "status": "healthy",
         "service": "ntrust-shield-v1",
         "environment": "staging",
         "uptime_check": "pass"
     }

@app.get("/metrics")
async def metrics_endpoint():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

@app.get("/")
async def root():
    return {"message": "nTrust Shield MVP initialized. Phase 1: Production Foundation."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
