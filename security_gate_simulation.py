#!/usr/bin/env python3
"""
TASK-1D9ECE: CI/CD Security Gates & Container Hardening Validation
Simulates a security scan that detects a critical vulnerability and triggers BUILD FAILED.
"""

import sys

def run_security_scan(image_tag):
    print(f"[INFO] Starting security gate validation for image: {image_tag}")
    
    known_vulns = [
        {"id": "CVE-2024-9999", "severity": "CRITICAL", "package": "libopenssl", "description": "Remote code execution via buffer overflow"}
    ]
    
    scan_results = []
    gate_triggered = False
    
    for vuln in known_vulns:
        print(f"[SCAN] Checking package: {vuln['package']}...")
        if vuln['severity'] == 'CRITICAL':
            scan_results.append(vuln)
            gate_triggered = True
            print(f"[ALERT] CRITICAL VULNERABILITY DETECTED: {vuln['id']} in {vuln['package']}")

    if gate_triggered:
        print("\n" + "="*50)
        print("SECURITY GATE TRIGGERED: BUILD ABORTED")
        print("="*50)
        print(f"Reason: Critical vulnerabilities found ({len(scan_results)})")
        print("Action: Pipeline halted. Remediation required.")
        return 1 
    else:
        print("\n[PASS] Security gate passed. 0 Critical CVEs found.")
        return 0

if __name__ == "__main__":
    exit_code = run_security_scan("dev/ntrust-mvp:v1")
    sys.exit(exit_code)
