"""
nTrust Pilot Cohort Onboarding & Secure Access Provisioning Module
Author: Alex (Lead Security Architect)
Purpose: Generate role-based API keys, enforce NIST RMF compliance, and log provisioning events.
"""

import hashlib
import secrets
import json
import logging
from datetime import datetime, timedelta

# Configure audit logging
logging.basicConfig(
    filename="/app/data/orgs/org_ntrust/logs/provisioning_audit.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("nTrust_Audit")

class SecureAccessProvisioner:
    def __init__(self):
        self.audit_log = []
        self.roles = {
            "admin": {"tier": 3, "permissions": ["read", "write", "delete", "manage_users"]},
            "analyst": {"tier": 2, "permissions": ["read", "analyze"]},
            "viewer": {"tier": 1, "permissions": ["read"]}
        }

    def generate_api_key(self, user_id: str, role: str) -> dict:
        """Generates a cryptographically secure API key with embedded metadata."""
        if role not in self.roles:
            raise ValueError(f"Invalid role: {role}. Must be one of {list(self.roles.keys())}")

        raw_key = secrets.token_hex(32)
        hashed_key = hashlib.sha256(raw_key.encode()).hexdigest()
        metadata = json.dumps({
            "user_id": user_id,
            "role": role,
            "created_at": datetime.utcnow().isoformat(),
            "expires_at": (datetime.utcnow() + timedelta(days=90)).isoformat(),
            "rbac_tier": self.roles[role]["tier"]
        })

        logger.info(f"Generated API key for user {user_id} with role {role}.")
        return {"hashed_key": hashed_key, "raw_key_preview": f"{raw_key[:8]}...{raw_key[-8:]}", "metadata": metadata}

    def validate_consent_workflow(self, user_id: str, consent_given: bool) -> bool:
        """Validates data minimization and explicit consent per NIST RMF."""
        if not consent_given:
            logger.warning(f"Consent denied for user {user_id}. Provisioning blocked.")
            return False
        logger.info(f"Explicit consent validated for user {user_id}.")
        return True

    def log_provisioning_event(self, event_type: str, details: dict):
        """Logs all provisioning events to audit vault."""
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        log_entry = f"{timestamp} | {event_type} | {json.dumps(details)}"
        self.audit_log.append(log_entry)
        logger.info(log_entry)

# Example Execution
if __name__ == "__main__":
    provisioner = SecureAccessProvisioner()

    # 1. Validate Consent
    if not provisioner.validate_consent_workflow("user_pilot_01", True):
        print("❌ Consents check failed. Exiting.")
        exit(1)

    # 2. Generate Secure Access
    key_data = provisioner.generate_api_key("user_pilot_01", "analyst")
    print(f"✅ Pilot onboarding successful. Key generated: {key_data['raw_key_preview']}...")

    # 3. Log Event
    provisioner.log_provisioning_event("PILOT_ONBOARDING_COMPLETE", {"user": "user_pilot_01", "status": "active"})
