from fastapi import FastAPI
import os

app = FastAPI(title="TrustAudit Engine", description="Core vulnerability scanning & reporting MVP")

@app.get("/")
def root():
    return {"status": "operational", "service": "TrustAudit Engine MVP", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy", "engine": "trustaudit-mvp", "uptime": "active"}

@app.post("/shield/scan")
def trigger_scan():
    return {"message": "Scan initiated", "job_id": "scan-001", "status": "queued"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
