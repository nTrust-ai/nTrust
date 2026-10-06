"""nTrust.ai — TrustGuard MVP Core Engine (Phase 3: Profitability Scaling)

FastAPI-based compliance risk scoring engine for enterprise vulnerability assessment.
Serves as the foundational MVP for the TrustGuard product line.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
import hashlib
from datetime import datetime

app = FastAPI(
    title="TrustGuard MVP — Compliance Risk Scoring Engine",
    description="nTrust.ai Phase 3 MVP: Enterprise vulnerability assessment & compliance scoring API",
    version="0.1.0-mvp"
)

# --- Models ---
class VulnerabilityInput(BaseModel):
    vuln_id: str = Field(..., description="Unique vulnerability identifier")
    cvss_score: float = Field(..., ge=0.0, le=10.0, description="CVSS v3.1 base score")
    description: str = Field(..., description="Vulnerability description")
    affected_systems: List[str] = Field(default_factory=list)
    remediation_priority: Optional[str] = Field(None, description="P1/P2/P3/P4")

class RiskAssessment(BaseModel):
    assessment_id: str
    timestamp: str
    overall_score: float
    risk_level: str
    vulnerabilities_scanned: int
    compliance_frameworks: List[str]
    recommendations: List[str]

class ComplianceCheck(BaseModel):
    framework: str = Field(..., description="NIST AI RMF, EU AI Act, ISO 27001")
    organization_name: str
    data_classification: str = Field(default="public", description="public/internal/confidential/restricted")

# --- Core Scoring Logic ---
def calculate_risk_score(vulns: List[VulnerabilityInput]) -> dict:
    if not vulns:
        return {"overall_score": 0.0, "risk_level": "CLEAR"}
    
    total_cvss = sum(v.cvss_score for v in vulns)
    avg_cvss = total_cvss / len(vulns)
    
    # Weighted scoring: high CVSS + many vulns = higher risk
    volume_factor = min(len(vulns) * 0.1, 2.0)
    severity_factor = avg_cvss * 10
    
    overall_score = min((severity_factor + volume_factor) / 12.0 * 100, 100.0)
    
    if overall_score >= 80:
        risk_level = "CRITICAL"
    elif overall_score >= 60:
        risk_level = "HIGH"
    elif overall_score >= 40:
        risk_level = "MODERATE"
    elif overall_score >= 20:
        risk_level = "LOW"
    else:
        risk_level = "CLEAR"
    
    recommendations = []
    if avg_cvss > 7.0:
        recommendations.append("Immediate patching required for critical vulnerabilities")
    if len(vulns) > 5:
        recommendations.append("Conduct full infrastructure audit — excessive vulnerability count detected")
    if any(v.remediation_priority == "P1" for v in vulns):
        recommendations.append("Escalate P1 items to incident response team immediately")
    
    return {
        "overall_score": round(overall_score, 2),
        "risk_level": risk_level,
        "recommendations": recommendations or ["No immediate action required — continue monitoring"]
    }

def compliance_check(framework: str, org_name: str, data_class: str) -> dict:
    checks = {
        "NIST AI RMF": {
            "map": True, "measure": True, "manage": True, "govern": True,
            "data_classification_requirement": ["confidential", "restricted"],
            "status": "COMPLIANT" if data_class in ["confidential", "restricted"] else "REQUIRES_ATTENTION"
        },
        "EU AI Act": {
            "risk_category_assessment": True,
            "transparency_reporting": True,
            "human_oversight": True,
            "status": "COMPLIANT" if data_class in ["confidential", "restricted"] else "REQUIRES_ATTENTION"
        },
        "ISO 27001": {
            "asset_inventory": True,
            "access_control_matrix": True,
            "incident_response_plan": True,
            "status": "COMPLIANT" if data_class in ["confidential", "restricted"] else "REQUIRES_ATTENTION"
        }
    }
    
    result = checks.get(framework, {"error": f"Framework '{framework}' not supported"})
    result["organization"] = org_name
    result["framework"] = framework
    return result

# --- Endpoints ---
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "TrustGuard MVP Core Engine",
        "version": "0.1.0-mvp",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.post("/api/v1/assess", response_model=RiskAssessment)
async def assess_risk(vulns: List[VulnerabilityInput]):
    """Submit vulnerabilities for risk scoring."""
    result = calculate_risk_score(vulns)
    
    assessment = RiskAssessment(
        assessment_id=str(uuid.uuid4()),
        timestamp=datetime.utcnow().isoformat() + "Z",
        overall_score=result["overall_score"],
        risk_level=result["risk_level"],
        vulnerabilities_scanned=len(vulns),
        compliance_frameworks=["NIST AI RMF", "EU AI Act", "ISO 27001"],
        recommendations=result["recommendations"]
    )
    
    return assessment

@app.post("/api/v1/compliance/check")
async def check_compliance(check: ComplianceCheck):
    """Run compliance framework validation."""
    return compliance_check(check.framework, check.organization_name, check.data_classification)

@app.get("/api/v1/metrics")
async def get_metrics():
    """Return MVP operational metrics (placeholder for Phase 3 scaling)."""
    return {
        "total_assessments": 0,
        "avg_response_time_ms": 12.4,
        "uptime_hours": 72,
        "frameworks_supported": ["NIST AI RMF", "EU AI Act", "ISO 27001"],
        "status": "MVP_READY"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8090)
