from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI()

DASH = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>nTrust.ai | Phase 3 MVP</title><style>body{margin:0;font-family:system-ui;background:#f8fafc;color:#0f172a;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center}.card{background:#fff;padding:3rem;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,.1)}.h1{font-size:2.5rem;margin-bottom:.5rem;color:#2563eb}.p{color:#64748b;font-size:1.1rem;margin-bottom:1.5rem}.btn{padding:.75rem 1.5rem;background:#2563eb;color:#fff;border-radius:8px;text-decoration:none;font-weight:600}</style></head><body><div class="card"><h1>nTrust.ai</h1><p>Enterprise AI Cybersecurity & Autonomous Governance</p><p>Phase 3: Profitability Scaling Active</p><a href="#" class="btn">Enter Pilot Dashboard</a></div></body></html>"""

@app.get("/")
async def root(): return HTMLResponse(DASH)

@app.get("/api/health")
async def health(): return JSONResponse({"status":"active","version":"3.1.0","mvp_gate":"live"})

if __name__=="__main__": uvicorn.run(app, host="0.0.0.0", port=8085)
