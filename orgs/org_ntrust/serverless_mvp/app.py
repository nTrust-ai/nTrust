import os, time, asyncio, logging
from typing import Dict, Any, List
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler()])
logger = logging.getLogger("serverless_mvp")

INFRA_STATE = {"status": "provisioning", "uptime_start": time.time(), "scaling_active": False, "auto_scale_threshold": 0.75, "current_load": 0.0, "max_concurrent_clients": 1000, "region": "us-east-1", "version": "1.0.0"}

class ScalingEngine:
    def __init__(self): self.load_history = []
    async def evaluate_load(self, current_requests):
        now = time.time()
        if len(self.load_history) > 0 and now - self.load_history[-1] < 60: return {"action": "cooldown", "new_capacity": INFRA_STATE["max_concurrent_clients"]}
        ratio = current_requests / INFRA_STATE["max_concurrent_clients"]; self.load_history.append(now)
        if ratio > 0.8: INFRA_STATE["scaling_active"] = True; INFRA_STATE["max_concurrent_clients"] *= 2; logger.warning(f"📈 AUTO-SCALE TRIGGERED: Load {ratio:.2%} exceeded threshold. Scaling capacity to {INFRA_STATE['max_concurrent_clients']}"); return {"action": "scale_up", "new_capacity": INFRA_STATE["max_concurrent_clients"], "reason": "load_threshold_exceeded"}
        elif ratio < 0.3 and INFRA_STATE["scaling_active"]: INFRA_STATE["scaling_active"] = False; INFRA_STATE["max_concurrent_clients"] //= 2; logger.info(f"📉 AUTO-SCALE DECOMMISSION: Load {ratio:.2%} below threshold. Capacity reduced to {INFRA_STATE['max_concurrent_clients']}"); return {"action": "scale_down", "new_capacity": INFRA_STATE["max_concurrent_clients"], "reason": "load_threshold_below"}
        return {"action": "stable", "new_capacity": INFRA_STATE["max_concurrent_clients"]}

scaling_engine = ScalingEngine()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Serverless MVP Infrastructure Initializing..."); INFRA_STATE["status"] = "active"; INFRA_STATE["uptime_start"] = time.time(); yield; INFRA_STATE["status"] = "shutting_down"; logger.info("🛑 Infrastructure shutdown complete.")

app = FastAPI(title="TrustGuard Serverless MVP", version="1.0.0", lifespan=lifespan)

@app.get("/health")
async def health_check():
    uptime = time.time() - INFRA_STATE["uptime_start"]
    return {"status": "healthy", "version": INFRA_STATE["version"], "region": INFRA_STATE["region"], "uptime_seconds": round(uptime, 2), "scaling_active": INFRA_STATE["scaling_active"], "max_capacity": INFRA_STATE["max_concurrent_clients"]}

@app.get("/metrics")
async def get_metrics(): return {"infrastructure_state": INFRA_STATE, "load_history_points": len(scaling_engine.load_history)}

@app.post("/invoke/{function_name}")
async def invoke_serverless_function(function_name: str, payload: Dict[str, Any]):
    await asyncio.sleep(0.05); current_requests = int(os.getenv("SIMULATED_LOAD", "1")); evaluation = await scaling_engine.evaluate_load(current_requests)
    return {"function": function_name, "status": "success", "execution_ms": 45, "scaling_evaluation": evaluation, "request_id": f"req_{int(time.time()*1000)}"}

@app.post("/scale/triggers")
async def manual_scale_trigger(request: Request): INFRA_STATE["scaling_active"] = not INFRA_STATE["scaling_active"]; return {"manual_override": True, "new_state": INFRA_STATE["scaling_active"]}
