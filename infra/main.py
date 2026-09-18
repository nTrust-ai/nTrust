from fastapi import FastAPI, Request
import os
import time
import logging
from datetime import datetime

app = FastAPI(title="nTrust-Infra", version="2.1.0")

# Configure audit logging
LOG_DIR = "/app/data/orgs/org_ntrust/logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=f"{LOG_DIR}/infra_audit.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "ntrust-infra-optimizer", "port": 8086, "uptime": time.time()}

@app.post("/revenue/log")
async def log_revenue(request: Request):
    try:
        data = await request.json()
        timestamp = datetime.utcnow().isoformat()
        entry = f"REVENUE | {timestamp} | {data}"
        logging.info(entry)
        return {"status": "logged", "timestamp": timestamp}
    except Exception as e:
        logging.error(f"Revenue log error: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/optimize")
async def optimize_system():
    logging.info("SYSTEM_OPTIMIZE | Triggered manual optimization cycle")
    return {"status": "optimized", "cycle": "2026-Q3-PROFITABILITY"}
