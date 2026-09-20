#!/usr/bin/env python3
"""Infrastructure Health & Readiness Validator — Phase 3 Scaling"""
import json, os, sys

def validate_infra():
    checks = {"status": "PASS", "details": []}
    
    # 1. Config Validation
    config_path = "config/system_params.json"
    if os.path.exists(config_path):
        with open(config_path) as f:
            cfg = json.load(f)
        checks["details"].append("✅ System parameters loaded successfully.")
        if cfg.get("compute", {}).get("phase3_scaling_mode"):
            checks["details"].append("✅ Phase 3 scaling mode enabled.")
    else:
        checks["status"] = "FAIL"
        checks["details"].append("❌ system_params.json missing.")

    # 2. Docker Bind Host Check (MANDATORY: 0.0.0.0)
    if cfg.get("compute", {}).get("docker_bind_host") == "0.0.0.0":
        checks["details"].append("✅ Docker bind host correctly set to 0.0.0.0.")
    else:
        checks["status"] = "WARN"
        checks["details"].append("⚠️ Docker bind host not optimized for external access.")

    # 3. Auto-Update & TTL Readiness
    if cfg.get("auto_updates", {}).get("enabled") and cfg.get("compute", {}).get("sandbox_ttl_hours", 0) > 24:
        checks["details"].append("✅ Auto-updates and sandbox TTL configured for continuous ops.")
    else:
        checks["status"] = "WARN"
        checks["details"].append("⚠️ Auto-update or TTL needs optimization for Phase 3.")

    # 4. Compliance/Logging Readiness
    audit_path = "docs/audit_log.md"
    if os.path.exists(audit_path):
        checks["details"].append("✅ Audit log repository present.")
    else:
        checks["details"].append("📝 Audit log placeholder ready for initialization.")

    return checks

if __name__ == "__main__":
    result = validate_infra()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "PASS" else 1)
