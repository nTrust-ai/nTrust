#!/usr/bin/env python3
"""
nTrust.ai - QA & Uptime Monitoring Automation
Target: Staging Environment (staging.ntrust.ai)
Scope: HTTP Health Check, Response Time, SSL Validity
"""

import requests
import time
import json
import os
from datetime import datetime

CONFIG = {
    "target_url": "https://staging.ntrust.ai",
    "timeout": 10,
    "check_interval": 300,  # 5 minutes
    "log_file": "/app/data/orgs/org_ntrust/workspace/monitoring/uptime_log.json"
}

def check_health():
    """Performs a single health check cycle."""
    timestamp = datetime.utcnow().isoformat()
    result = {
        "timestamp": timestamp,
        "status": "UNKNOWN",
        "response_time_ms": None,
        "ssl_valid": None,
        "error": None
    }

    try:
        start_time = time.time()
        # Verify SSL and HTTP 200
        response = requests.get(CONFIG["target_url"], timeout=CONFIG["timeout"], verify=True)
        response_time = (time.time() - start_time) * 1000
        
        result["response_time_ms"] = round(response_time, 2)
        result["ssl_valid"] = True
        result["status"] = "UP" if response.status_code == 200 else "DEGRADED"
        
        if response.status_code != 200:
            result["error"] = f"Unexpected status code: {response.status_code}"
            
    except requests.exceptions.SSLError as e:
        result["status"] = "DOWN"
        result["ssl_valid"] = False
        result["error"] = f"SSL Error: {str(e)}"
    except requests.exceptions.ConnectionError as e:
        result["status"] = "DOWN"
        result["error"] = f"Connection Error: {str(e)}"
    except requests.exceptions.Timeout as e:
        result["status"] = "TIMEOUT"
        result["error"] = f"Timeout after {CONFIG['timeout']}s"
    except Exception as e:
        result["status"] = "ERROR"
        result["error"] = str(e)

    return result

def log_result(result):
    """Appends result to local JSON log."""
    log_path = CONFIG["log_file"]
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    history = []
    if os.path.exists(log_path):
        try:
            with open(log_path, 'r') as f:
                history = json.load(f)
        except json.JSONDecodeError:
            history = []
    
    history.append(result)
    
    # Keep last 1000 entries to prevent log bloat
    if len(history) > 1000:
        history = history[-1000:]
        
    with open(log_path, 'w') as f:
        json.dump(history, f, indent=2)

def main():
    print(f"[nTrust Monitor] Starting check at {datetime.utcnow().isoformat()}")
    result = check_health()
    log_result(result)
    
    status_icon = "✅" if result["status"] == "UP" else "🚨"
    print(f"[nTrust Monitor] {status_icon} Status: {result['status']} | RT: {result['response_time_ms']}ms | SSL: {result['ssl_valid']}")
    
    if result["error"]:
        print(f"   Detail: {result['error']}")

if __name__ == "__main__":
    main()