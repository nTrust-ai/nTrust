"""nTrust.ai MVP Dashboard & Monetization Gateway — FastAPI Backend"""
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(title="nTrust.ai MVP", version="3.1.0")

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>nTrust.ai | Enterprise Security & AI Governance</title>
      <style>
          :root { --primary: #2563eb; --dark: #0f172a; --light: #f8fafc; --accent: #10b981; }
         body { margin: 0; font-family: 'Inter', system-ui, sans-serif; background: var(--light); color: var(--dark); }
         .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
         header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 2rem; border-bottom: 1px solid #e2e8f0; }
         h1 { font-size: 2.5rem; margin: 0; letter-spacing: -0.02em; }
         .nav-links a { margin-left: 1.5rem; text-decoration: none; color: var(--dark); font-weight: 500; }
         .hero { padding: 4rem 0; text-align: center; }
         .hero h2 { font-size: 3rem; margin-bottom: 1rem; }
         .hero p { font-size: 1.25rem; color: #64748b; max-width: 700px; margin: 0 auto 2rem; }
         .cta-group { display: flex; gap: 1rem; justify-content: center; }
         .btn { padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; text-decoration: none; transition: all 0.2s; }
         .btn-primary { background: var(--primary); color: white; }
         .btn-secondary { background: white; border: 1px solid #cbd5e1; color: var(--dark); }
         .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 4rem; }
         .card { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
         .card h3 { margin-top: 0; color: var(--primary); }
         .monetization-gate { background: var(--dark); color: white; padding: 3rem; border-radius: 16px; text-align: center; margin-top: 4rem; }
         footer { margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #e2e8f0; text-align: center; color: #94a3b8; }
      </style>
</head>
<body>
      <div class="container">
         <header>
             <h1>nTrust.ai</h1>
             <nav class="nav-links">
                 <a href="#products">Products</a>
                 <a href="#trustguard">TrustGuard</a>
                 <a href="#partnerships">Partners</a>
                 <a href="#contact">Contact</a>
             </nav>
         </header>
         <section class="hero" id="products">
             <h2>Enterprise-Grade AI Cybersecurity & Governance</h2>
             <p>Autonomous threat detection, compliance automation, and zero-trust infrastructure scaling. Built for the modern enterprise.</p>
             <div class="cta-group">
                 <a href="#" class="btn btn-primary">Request Enterprise Audit</a>
                 <a href="#" class="btn btn-secondary">View TrustGuard MVP</a>
             </div>
         </section>
         <section class="features">
             <div class="card">
                 <h3>🛡️ TrustGuard AI</h3>
                 <p>Real-time vulnerability scanning and compliance reporting. Coming Soon: Enterprise Tier.</p>
             </div>
             <div class="card">
                 <h3>📊 ASPM & AppSOC</h3>
                 <p>Application Security Posture Management with SOC-grade alerting pipeline.</p>
             </div>
             <div class="card">
                 <h3>🤖 Autonomous Governance</h3>
                 <p>NIST AI RMF & EU AI Act compliant automated audit workflows.</p>
             </div>
         </section>
         <div class="monetization-gate">
             <h2>🚀 Phase 3: Profitability Scaling Active</h2>
             <p>Enterprise SOWs, B2B Pipeline Activation, and TrustGuard Commercial Roadmap are now live for pilot integration.</p>
             <a href="#" class="btn btn-primary" style="margin-top: 1rem; display: inline-block;">Access Pilot Dashboard</a>
         </div>
         <footer>
             <p>&copy; 2026 nTrust.ai. All rights reserved. | ubaz inc. Joint Venture Partner</p>
         </footer>
      </div>
</body>
</html>
"""

@app.get("/")
async def dashboard():
    return HTMLResponse(DASHBOARD_HTML)

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "3.1.0", "mvp_gate": "active", "phase3": "scaling"}

@app.get("/api/compliance/status")
async def compliance_status():
    return {
        "nist_ai_rmf": "compliant",
        "eu_ai_act": "monitoring",
        "ph3_revenue_target": "$500K_Q3"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8085)