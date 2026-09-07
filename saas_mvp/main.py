from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="nTrust.ai SaaS Execution Engine", version="0.1.0")


# Models
class ExecutionTask(BaseModel):
    task_id: str
    name: str
    status: str = "pending"
    created_at: datetime = datetime.utcnow()
    priority: int = 1


class PricingTier(BaseModel):
    tier_name: str
    price: float
    features: List[str]
    max_executions: int


# In-memory storage (for MVP)
execution_tasks: List[ExecutionTask] = []
pricing_tiers: List[PricingTier] = []


# Health Check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


# Execution Engine Endpoints
@app.post("/tasks", response_model=ExecutionTask)
async def create_task(task: ExecutionTask):
    execution_tasks.append(task)
    return task


@app.get("/tasks", response_model=List[ExecutionTask])
async def list_tasks():
    return execution_tasks


@app.get("/tasks/{task_id}", response_model=ExecutionTask)
async def get_task(task_id: str):
    for task in execution_tasks:
        if task.task_id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}/status")
async def update_task_status(task_id: str, status: str):
    for task in execution_tasks:
        if task.task_id == task_id:
            task.status = status
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Pricing Engine Endpoints
@app.post("/pricing/tiers", response_model=PricingTier)
async def create_pricing_tier(tier: PricingTier):
    pricing_tiers.append(tier)
    return tier


@app.get("/pricing/tiers", response_model=List[PricingTier])
async def list_pricing_tiers():
    return pricing_tiers


@app.get("/pricing/calculate")
async def calculate_price(executions: int, tier_name: Optional[str] = None):
    # Simple pricing logic for MVP
    if not tier_name:
        # Find the best tier for the number of executions
        suitable_tiers = [t for t in pricing_tiers if t.max_executions >= executions]
        if not suitable_tiers:
            raise HTTPException(status_code=400, detail="No suitable tier found")
        # Return the cheapest suitable tier
        tier = min(suitable_tiers, key=lambda t: t.price)
    else:
        tier = next((t for t in pricing_tiers if t.tier_name == tier_name), None)
        if not tier:
            raise HTTPException(status_code=404, detail="Tier not found")

    return {
        "tier": tier.tier_name,
        "price": tier.price,
        "executions": executions,
        "total": tier.price,  # Simplified for MVP
    }


# Seed initial data
@app.on_event("startup")
async def startup_event():
    # Seed some initial pricing tiers
    global pricing_tiers
    pricing_tiers = [
        PricingTier(
            tier_name="Starter",
            price=49.00,
            features=["Basic Compliance Checks"],
            max_executions=100,
        ),
        PricingTier(
            tier_name="Professional",
            price=199.00,
            features=["Advanced Scans", "Real-time Alerts"],
            max_executions=500,
        ),
        PricingTier(
            tier_name="Enterprise",
            price=999.00,
            features=["Full Suite", "Dedicated Support"],
            max_executions=99999,
        ),
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
