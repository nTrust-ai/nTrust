#!/usr/bin/env python3
"""
TrustAudit Engine Local Stack Validation Script
Validates Docker Compose configuration against nTrust security baselines.
Simulates deployment readiness checks for Phase 1 Infrastructure Mandate.
"""

import os
import yaml
import json
from pathlib import Path


def validate_compose_file(filepath: str) -> dict:
    """Parse and validate docker-compose.yml structure."""
    with open(filepath, "r") as f:
        compose_data = yaml.safe_load(f)

    validation_results = {
        "file_valid": True,
        "services_found": [],
        "networks_configured": False,
        "port_mappings": [],
        "security_baseline_pass": True,
    }

    if not compose_data.get("services"):
        validation_results["file_valid"] = False
        return validation_results

    for service_name, config in compose_data["services"].items():
        validation_results["services_found"].append(service_name)

        # Check port exposure
        if "ports" in config:
            for port in config["ports"]:
                validation_results["port_mappings"].append(port)

        # Validate network isolation
        networks = config.get("networks", [])
        if isinstance(networks, list):
            if "shield-net" in networks:
                validation_results["networks_configured"] = True

    return validation_results


def check_security_baseline(config: dict) -> bool:
    """Ensure configuration adheres to nTrust Phase 1 security mandates."""
    # Check for restricted ports or unsafe defaults
    risky_ports = ["22", "23", "25", "445", "3389"]
    for port_str in config["port_mappings"]:
        host_port = str(port_str).split(":")[0].strip('"')
        if host_port in risky_ports:
            return False
    return True


if __name__ == "__main__":
    compose_path = "/app/data/orgs/org_ntrust/trustaudit-engine/docker-compose.yml"
    print("🔍 Running TrustAudit Engine Local Stack Validation...")

    if os.path.exists(compose_path):
        results = validate_compose_file(compose_path)
        is_secure = check_security_baseline(results)

        print(f"✅ Compose file valid: {results['file_valid']}")
        print(f"🛡️ Services detected: {results['services_found']}")
        print(f"🌐 Network isolation configured: {results['networks_configured']}")
        print(f"🔒 Security baseline pass: {is_secure}")

        if results["file_valid"] and is_secure:
            print(
                "✅ Stack deployment readiness confirmed. Proceeding to Phase 2 pilot validation."
            )
        else:
            print("❌ Deployment halted. Security baseline violation detected.")
    else:
        print("⚠️ docker-compose.yml not found in expected path.")
