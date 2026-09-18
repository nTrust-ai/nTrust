from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI(title="nTrust.ai MVP", version="3.1.0")

@app.get("/")
async def root():
    return HTMLResponse("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>nTrust.ai — Enterprise AI Cybersecurity</title><style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;min-height:100vh;display:flex;flex-direction:column}.container{max-width:1200px;margin:0 auto;padding:2rem;width:100%}header{display:flex;justify-content:space-between;align-items:center;padding:1.5rem 0;border-bottom:1px solid rgba(255,255,255,0.1);margin-bottom:3rem}nav a{color:#94a3b8;text-decoration:none;margin-left:2rem;font-weight:500}.brand{font-size:1.6rem;font-weight:800;background:linear-gradient(90deg,#38bdf8,#7c3aed);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.hero{text-align:center;padding:4rem 0}.hero h1{font-size:3rem;margin-bottom:1rem;background:linear-gradient(90deg,#f1f5f9,#94a3b8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.hero p{color:#94a3b8;font-size:1.2rem;max-width:600px;margin:0 auto 2rem;line-height:1.6}.btn{display:inline-block;padding:1rem2rem;background:linear-gradient(90deg,#38bdf8,#7c3aed);color:#fff;border-radius:10px;font-weight:600;text-decoration:none;transition:transform .2s}.btn:hover{transform:scale(1.05)}.services{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem;margin-bottom:3rem}.card{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:1.5rem}.card h3{color:#38bdf8;margin-bottom:.75rem}.card p{color:#94a3b8;font-size:.9rem;line-height:1.5}.footer{text-align:center;padding:2rem 0;color:#475569;font-size:.85rem;border-top:1px solid rgba(255,255,255,0.05);margin-top:auto}</style></head><body><div class="container"><header><div class='brand'>nTrust.ai</div><nav><a href='/products'>Services</a><a href='/dashboard'>Dashboard</a><a href='/shield'>Security</a></nav></header><div class='hero'><h1>Enterprise AI Cybersecurity & Autonomous Governance</h1><p>NIST AI RMF | EU AI Act Compliant | SOC 2 Type II<br/>Phase 3: Profitability Scaling — Active</p><a href='/products' class='btn'>Explore Our Services</a></div><div class='services'><div class='card'><h3>🛡️ TrustGuard Security Platform</h3><p>AI-powered threat detection and incident response automation.</p></div><div class='card'><h3>📊 Revenue Intelligence</h3><p>Real-time pipeline analytics and conversion tracking.</p></div><div class='card'><h3>🔐 Compliance Automation</h3><p>NIST AI RMF gap analysis and EU AI Act readiness.</p></div></div></div><footer class='footer'>© 2026 nTrust.ai — All rights reserved</footer></body></html>""")

@app.get("/products")
async def products():
    try:
        with open("www-catalog/index.html") as f: return HTMLResponse(f.read())
    except: return HTMLResponse("<h1>Coming Soon</h1>")

@app.get("/dashboard")
async def dashboard():
    try:
        with open("dashboard/index.html") as f: return HTMLResponse(f.read())
    except: return HTMLResponse("<h1>Coming Soon</h1>")

@app.get("/health")
async def health():
    return JSONResponse({"status":"active","service":"nTrust.ai MVP","port":55127,"version":"3.1.0","mvp_gate":"live","phase":"Phase 3 Profitability Scaling"})

@app.get("/api/health")
async def api_health():
    return JSONResponse({"ok":True,"service":"nTrust.ai","uptime":"active","compliance":["NIST AI RMF","EU AI Act","ISO 27001"]})

if __name__=="__main__":
    print("🚀 Starting nTrust.ai MVP on port 55127...")
    uvicorn.run(app, host="0.0.0.0", port=55127)
