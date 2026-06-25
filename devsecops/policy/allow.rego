package ntrust.security.gate

import rego.v1

# NIST AI RMF & EU AI Act HITL Compliance Policy
# Enforces mandatory security gates before production deployment

import input

# Deny deployments that lack critical security scans
deny if {
    not input.metadata.scan_trivy
    metadata.msg := "Deployment blocked: Trivy vulnerability scan missing"
}

# Deny deployments exceeding critical threshold
deny if {
    input.metadata.vulnerability_count > 0
    metadata.msg := "Deployment blocked: Critical vulnerabilities detected"
}

# Enforce HITL approval gate
deny if {
    not input.metadata.hitl_approved
    metadata.msg := "Deployment blocked: Human-in-the-Loop approval required per EU AI Act"
}

# Enforce RBAC tier validation
deny if {
    input.metadata.rbac_tier < 3
    metadata.msg := "Deployment blocked: Insufficient RBAC clearance (min Tier 3)"
}
