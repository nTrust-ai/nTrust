"""
nTrust.ai Automated SaaS Dashboard - MVP Core
Phase 1: Infrastructure & Product Launch
Author: Alex (Lead Security Architect)
Date: 2026-06-25
"""

from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Mock Security Metrics (Phase 1 MVP)
SECURITY_METRICS = {
    "threat_score": 0,
    "vulnerability_count": 0,
    "compliance_status": "Pending Audit",
    "uptime": "100%"
}

@app.route('/')
def home():
    return jsonify({
        "status": "operational",
        "mission": "nTrust.ai - It is the numbers we trust",
        "version": "0.1.0-MVP"
    })

@app.route('/api/security/dashboard')
def security_dashboard():
    """Returns current security posture metrics."""
    return jsonify(SECURITY_METRICS)

@app.route('/api/security/scan', methods=['POST'])
def trigger_scan():
    """Simulates a security scan trigger."""
    # In production, this would trigger a Docker container scan
    return jsonify({"status": "scan_initiated", "task_id": "SCAN-2026-001"})

if __name__ == '__main__':
    # Run on 0.0.0.0 for Docker accessibility
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)