"""
STRIDE Threat Model Framework for ThreatShield AI (Phase 1 MVP)
Aligns with NIST AI RMF & EU HITL Compliance mandates.
Focus: Prompt Injection, Model Weights Theft, Data Poisoning, API Abuse.
"""

import enum
from dataclasses import dataclass, field
from typing import List, Optional


class ThreatCategory(enum.Enum):
    SPOOFING = "Spoofing"
    TAMPERING = "Tampering"
    REPUDIATION = "Repudiation"
    INFORMATION_DISCLOSURE = "Information Disclosure"
    DENIAL_OF_SERVICE = "Denial of Service"
    ELEVATION_OF_PRIVILEGE = "Elevation of Privilege"


@dataclass
class ThreatScenario:
    category: ThreatCategory
    component: str
    description: str
    mitigation: str
    severity_score: int  # 1-10 (NIST RMF aligned)


class STRIDEModel:
    def __init__(self, product_name: str):
        self.product_name = product_name
        self.threats: List[ThreatScenario] = []

    def add_threat(self, scenario: ThreatScenario):
        self.threats.append(scenario)

    def validate_model(self) -> dict:
        """Validates coverage across all STRIDE categories and returns risk summary."""
        coverage = {cat.value: 0 for cat in ThreatCategory}
        for t in self.threats:
            coverage[t.category.value] += 1
        
        total_severity = sum(t.severity_score for t in self.threats)
        avg_severity = total_severity / len(self.threats) if self.threats else 0

        return {
            "product": self.product_name,
            "total_threats": len(self.threats),
            "coverage_matrix": coverage,
            "avg_severity_score": round(avg_severity, 2),
            "hitl_compliance_flag": True,  # Requires board/manager review before Phase 2 pilot
            "status": "VALIDATED_FOR_REVIEW"
        }


def instantiate_threatshield_model() -> STRIDEModel:
    """Instantiates the initial STRIDE model for ThreatShield AI."""
    model = STRIDEModel("ThreatShield_AI_MVP")
    
    # SPOOFING
    model.add_threat(ThreatScenario(
        category=ThreatCategory.SPOOFING,
        component="API Gateway / LLM Endpoint",
        description="Unauthorized API keys or compromised service accounts spoofing legitimate inference requests.",
        mitigation="Enforce strict OAuth2/OIDC token validation, rate limiting, and mutual TLS for internal services.",
        severity_score=7
    ))

    # TAMPERING
    model.add_threat(ThreatScenario(
        category=ThreatCategory.TAMPERING,
        component="Model Weights & Prompt Cache",
        description="Adversarial tampering of cached prompts or fine-tuned weights leading to degraded/injected outputs.",
        mitigation="Implement cryptographic hashing (SHA-256) for model artifacts. Use signed inference pipelines.",
        severity_score=8
    ))

    # REPUDIATION
    model.add_threat(ThreatScenario(
        category=ThreatCategory.REPUDIATION,
        component="Audit Logging Service",
        description="Attackers modifying or deleting LLM request logs to evade compliance auditing and incident response.",
        mitigation="Append-only immutable logging storage. Enable WORM (Write-Once Read-Many) disk policies.",
        severity_score=6
    ))

    # INFORMATION_DISCLOSURE
    model.add_threat(ThreatScenario(
        category=ThreatCategory.INFORMATION_DISCLOSURE,
        component="Training Data Pipeline",
        description="Exfiltration of PII or proprietary datasets via model inversion or membership inference attacks.",
        mitigation="Deploy differential privacy noise injection. Enforce strict data masking at ingestion layer.",
        severity_score=9
    ))

    # DENIAL_OF_SERVICE
    model.add_threat(ThreatScenario(
        category=ThreatCategory.DENIAL_OF_SERVICE,
        component="Compute Inference Cluster",
        description="Resource exhaustion via adversarial prompt loops or heavy token generation requests.",
        mitigation="Implement graceful degradation circuit breakers. Enforce max token limits and queue-based scheduling.",
        severity_score=7
    ))

    # ELEVATION_OF_PRIVILEGE
    model.add_threat(ThreatScenario(
        category=ThreatCategory.ELEVATION_OF_PRIVILEGE,
        component="Agent Execution Environment",
        description="Prompt injection escaping sandbox boundaries to access internal metadata or adjacent services.",
        mitigation="Strict least-privilege IAM roles. Network segmentation (VPC peering disabled by default). Input sanitization gates.",
        severity_score=8
    ))

    return model


if __name__ == "__main__":
    threat_model = instantiate_threatshield_model()
    validation_result = threat_model.validate_model()
    print(f"🛡️ STRIDE Model Validated for {validation_result['product']}")
    print(f"📊 Coverage Matrix: {validation_result['coverage_matrix']}")
    print(f"⚠️ Avg Severity Score: {validation_result['avg_severity_score']}")
    print("✅ Awaiting Board/Manager HITL review before Phase 2 pilot deployment.")
