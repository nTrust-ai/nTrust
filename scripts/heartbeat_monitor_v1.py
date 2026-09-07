#!/usr/bin/env python3
"""
Heartbeat Monitor v1.0 — Phase 2 Pilot Validation
Author: Alex (Lead Security Architect)
Purpose: 24/7 Uptime Tracking & Error Logging for Pilot Cohort
Compliance: NIST AI RMF / EU HITL Audit Trail
"""

import requests
import logging
import time
import datetime
import os
from typing import Optional, Dict

# Configuration
TARGET_ENDPOINTS = [
    "https://ntrust.ai",
    "https://staging.ntrust.ai",
    "http://localhost:8000",  # Local MVP fallback
]
LOG_DIR = "./logs/pilot_monitoring"
MONITOR_INTERVAL_SECONDS = 300  # 5 minutes
MAX_RETRIES = 3
TIMEOUT_SEC = 10

# Setup Logging
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "heartbeat_status.log"),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(console_handler)


class HeartbeatMonitor:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "nTrust-Heartbeat/1.0"})
        self.stats: Dict[str, int] = {endpoint: 0 for endpoint in TARGET_ENDPOINTS}

    def check_endpoint(self, url: str) -> bool:
        try:
            response = self.session.get(url, timeout=TIMEOUT_SEC, allow_redirects=True)
            if response.status_code == 200:
                logging.info(f"✅ {url} — Online (HTTP 200)")
                return True
            else:
                logging.warning(f"⚠️ {url} — Degraded (HTTP {response.status_code})")
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ {url} — UNREACHABLE ({str(e)})")
            return False

    def run_cycle(self):
        logging.info("--- 🔍 PILOT MONITORING CYCLE START ---")
        for endpoint in TARGET_ENDPOINTS:
            success = self.check_endpoint(endpoint)
            if success:
                self.stats[endpoint] += 1
        logging.info("--- 🔍 PILOT MONITORING CYCLE COMPLETE ---\n")

    def start_monitoring(self):
        logging.info(
            "🚀 Heartbeat Monitor v1.0 initialized. Starting 24/7 uptime tracking."
        )
        while True:
            self.run_cycle()
            time.sleep(MONITOR_INTERVAL_SECONDS)


if __name__ == "__main__":
    monitor = HeartbeatMonitor()
    try:
        monitor.start_monitoring()
    except KeyboardInterrupt:
        logging.info("🛑 Monitor stopped by operator. Final stats logged.")
        print("\nFinal Uptime Stats:")
        for ep, count in monitor.stats.items():
            print(f"  {ep}: {count} successful cycles")
