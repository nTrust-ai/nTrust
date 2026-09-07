#!/usr/bin/env python3
"""
TASK-35B1CD: Pilot Cohort Onboarding & Validation Logic
Demonstrates successful processing of a pilot cohort record.
"""

import json


def validate_pilot_cohort(cohort_data):
    print(f"[INFO] Validating Pilot Cohort ID: {cohort_data['id']}")

    required_fields = ["id", "email", "status", "compliance_signed"]
    errors = []

    for field in required_fields:
        if field not in cohort_data:
            errors.append(f"Missing required field: {field}")

    if not errors and cohort_data.get("compliance_signed") is True:
        print("[SUCCESS] All compliance checks passed.")
        print(f"[OUTPUT] Pilot Cohort {cohort_data['id']} marked as 'Validated'.")
        return "VALIDATED"
    else:
        print(f"[ERROR] Validation failed. Errors: {errors}")
        return "INVALIDATED"


if __name__ == "__main__":
    mock_pilot = {
        "id": "PILOT-001",
        "email": "pilot.user@ntrust.ai",
        "status": "active",
        "compliance_signed": True,
    }

    result = validate_pilot_cohort(mock_pilot)
    print(f"\nFinal Status: {result}")
