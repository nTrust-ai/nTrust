from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="nTrust.ai Automated SaaS Dashboard", version="1.0.0")

class ExecutionJob(BaseModel):
    id: str
    name: str
    status: str  # pending, running, completed, failed
    created_at: str
    last_run: Optional[str] = None

class DashboardStats(BaseModel):
    total_jobs: int
    active_jobs: int
    success_rate: float
    uptime: float

# Mock Database
jobs_db = [
    ExecutionJob(id="job-001", name="Daily Security Scan", status="completed", created_at="2026-06-25T00:00:00Z", last_run="2026-06-25T04:00:00Z"),
    ExecutionJob(id="job-002", name="Compliance Check", status="running", created_at="2026-06-25T01:00:00Z", last_run="2026-06-25T05:00:00Z"),
    ExecutionJob(id="job-003", name="Threat Model Update", status="pending", created_at="2026-06-25T02:00:00Z"),
]

@app.get("/")
def read_root():
    return {"message": "nTrust.ai Automated SaaS Dashboard API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": "2026-06-25T05:20:00Z"}

@app.get("/api/jobs", response_model=List[ExecutionJob])
def list_jobs():
    return jobs_db

@app.get("/api/jobs/{job_id}", response_model=ExecutionJob)
def get_job(job_id: str):
    for job in jobs_db:
        if job.id == job_id:
            return job
    raise HTTPException(status_code=404, detail="Job not found")

@app.post("/api/jobs")
def create_job(job: ExecutionJob):
    jobs_db.append(job)
    return {"message": "Job created successfully", "job": job}

@app.get("/api/stats", response_model=DashboardStats)
def get_stats():
    total = len(jobs_db)
    active = sum(1 for j in jobs_db if j.status == "running")
    completed = sum(1 for j in jobs_db if j.status == "completed")
    success_rate = (completed / total * 100) if total > 0 else 0.0
    return DashboardStats(
        total_jobs=total,
        active_jobs=active,
        success_rate=round(success_rate, 2),
        uptime=99.99
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)