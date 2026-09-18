"""
TrustGuard B2B Pricing & Commercialization Service
Phase 3 Revenue Launch Infrastructure
System Optimizer | Automated Deployment Artifact
"""

import os
import logging
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TrustGuardPricing")

app = FastAPI(
    title="TrustGuard B2B Pricing Service",
    description="Phase 3 Revenue Launch - Commercialization & Tiered Pricing Engine"
)

# --- Configuration & Tiers ---
PRICING_TIERS = {
     "starter": {"base_monthly": 499, "per_seat": 15, "features": ["Basic Threat Monitoring", "Email Alerts"]},
     "professional": {"base_monthly": 1499, "per_seat": 35, "features": ["Advanced ASPM", "SOC Integration", "24/7 Support"]},
     "enterprise": {"base_monthly": 4999, "per_seat": 80, "features": ["Full AppSOC Suite", "Dedicated CISO", "Custom SLA", "Audit Logging"]}
}

ADDONS = {
     "compliance_pack": 299,
     "incident_response": 599,
     "ai_threat_intel": 399
}

# --- Models ---
class PricingRequest(BaseModel):
    seats: int = Field(..., gt=0, description="Number of user seats required")
    tier: str = Field("professional", description="Pricing tier: starter, professional, enterprise")
    addons: List[str] = Field(default=[], description="Optional add-on packs")
    contract_months: int = Field(12, ge=1, le=36, description="Contract duration in months")

class PricingResponse(BaseModel):
    monthly_total: float
    annual_total: float
    breakdown: dict
    discount_applied: str

# --- Endpoints ---
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "TrustGuard Pricing Engine", "phase": "Phase 3 Commercialization"}

@app.post("/calculate-pricing", response_model=PricingResponse)
def calculate_pricing(req: PricingRequest):
    if req.tier not in PRICING_TIERS:
        raise HTTPException(status_code=400, detail=f"Invalid tier. Choose from: {list(PRICING_TIERS.keys())}")
    
    for addon in req.addons:
        if addon not in ADDONS:
            raise HTTPException(status_code=400, detail=f"Invalid addon: {addon}")

    tier_data = PRICING_TIERS[req.tier]
    base_cost = tier_data["base_monthly"]
    seat_cost = tier_data["per_seat"] * req.seats
    monthly_subtotal = base_cost + seat_cost
    
    # Addons
    addon_total = sum(ADDONS[a] for a in req.addons)
    monthly_total = monthly_subtotal + addon_total

    # Contract Discount Logic
    discount_map = {1: 0, 6: 5, 12: 10, 24: 15, 36: 20}
    discount_pct = discount_map.get(req.contract_months, 0)
    discounted_monthly = monthly_total * (1 - discount_pct / 100)
    
    return PricingResponse(
        monthly_total=round(discounted_monthly, 2),
        annual_total=round(discounted_monthly * 12, 2),
        breakdown={
            "base": base_cost, "seats": seat_cost, "addons": addon_total,
            "discount_percent": discount_pct, "contract_term_months": req.contract_months
         },
        discount_applied=f"{discount_pct}% annual contract discount"
     )

# --- Infrastructure / Commercialization Hooks ---
@app.get("/commercialization-status")
def commercialization_status():
    return {
         "phase": "Phase 3 Revenue Launch",
         "status": "ACTIVE",
         "target_revenue": "$500K+ Q3",
         "next_steps": ["Deploy to Docker Sandbox", "Enable Port 8085 Access", "Initiate B2B Outreach"]
     }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8085)
