"""
frts_core.py — nTrust.ai Feature Request Tracking System (FRTS) v1.0 core engine.
Owner: GovernanceOfficer. Scope: all 9 organizational products.
Compliance: NIST AI RMF mapping + EU AI Act Art.12 traceability + Art.14 HITL chain.
Lifecycle: NEW -> TRIAS -> ACCEPTED -> DEVELOPMENT -> TESTING -> RELEASED | REJECTED
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import hashlib, json, uuid

PRODUCT_REGISTRY = {
    "PROD-597152": "PrivacyGuard Suite",
    "PROD-335E45": "TrustAudit Engine",
    "PROD-DCCCF5": "nTrust Shield",
    "PROD-71C577": "nTrust.ai Website",
    "PROD-SPINE": "Spine Engine OSS",
    "PROD-275A24": "nTrust Core Platform",
    "PROD-DE7694": "TrustGuard",
    "PROD-75052F": "Enterprise Security Audit Service",
    "PROD-BFBA88": "nTrust.ai Web Dashboard MVP",
}

STATES = ["NEW", "TRIAS", "ACCEPTED", "DEVELOPMENT", "TESTING", "RELEASED", "REJECTED"]


@dataclass
class FeatureRequest:
    title: str
    description: str
    product_id: str
    priority: str = "P2"  # P0..P3
    expected_impact: str = ""
    timeline: str = ""
    nist_category: str = "GOVERN"  # NIST AI RMF function
    eu_ai_risk: str = "MINIMAL"  # EU AI Act risk class
    state: str = "NEW"
    requester: str = ""
    fr_id: str = field(default_factory=lambda: f"FR-{uuid.uuid4().hex[:8].upper()}")

    def __post_init__(self):
        if self.product_id not in PRODUCT_REGISTRY:
            raise ValueError(f"Unknown product_id: {self.product_id}")
        if self.state not in STATES:
            raise ValueError(f"Invalid state: {self.state}")


class ComplianceLogger:
    """SHA256 event registry with HITL chain (EU AI Act Art.12/14 traceability)."""

    def __init__(self):
        self.events = []

    def log(self, entity_id, actor, action, detail=""):
        ts = datetime.now(timezone.utc).isoformat()
        payload = json.dumps(
            {
                "id": entity_id,
                "actor": actor,
                "action": action,
                "detail": detail,
                "ts": ts,
            },
            sort_keys=True,
        )
        digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        self.events.append(
            {
                "actor": actor,
                "action": action,
                "detail": detail,
                "ts": ts,
                "sha256": digest,
                "event_id": f"EVT-{uuid.uuid4().hex[:10].upper()}",
            }
        )
        return self.events[-1]


class FRTS:
    def __init__(self):
        self.requests = {}
        self.audit = ComplianceLogger()

    def submit(self, fr: FeatureRequest, actor="intake"):
        self.requests[fr.fr_id] = fr
        self.audit.log(fr.fr_id, actor, "SUBMIT", f"state=NEW product={fr.product_id}")
        return fr.fr_id

    def transition(self, fr_id, new_state, actor, rationale=""):
        fr = self.requests.get(fr_id)
        if not fr:
            raise KeyError(fr_id)
        if new_state not in STATES:
            raise ValueError(f"Invalid state: {new_state}")
        fr.state = new_state
        self.audit.log(
            fr_id, actor, "TRANSITION", f"state={new_state} rationale={rationale}"
        )
        return fr

    def snapshot(self):
        return {fid: asdict(fr) for fid, fr in self.requests.items()}
