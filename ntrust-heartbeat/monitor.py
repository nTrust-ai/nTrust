"""
nTrust Shield — 24/7 Uptime Heartbeat & Error Logging Module
Deployed for Phase 2 Pilot Validation (TASK-1279D6)
Version: 1.0.0 | Date: 2026-06-24
"""

import time
import logging
import requests
from datetime import datetime

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("ntrust_heartbeat.log"), logging.StreamHandler()],
)
logger = logging.getLogger("nTrust.Heartbeat")

HEALTH_ENDPOINTS = ["http://localhost:8000/health", "https://staging.ntrust.ai/health"]


class UptimeMonitor:
    def __init__(self, interval_seconds=30):
        self.interval = interval_seconds
        self.alert_threshold = 2  # consecutive failures trigger alert
        self.failure_count = 0
        self.last_status = {}

    def check_health(self, url):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            duration_ms = (time.time() - start_time) * 1000
            if response.status_code == 200:
                self.failure_count = 0
                status = "HEALTHY"
            else:
                self.failure_count += 1
                status = f"UNHEALTHY (HTTP {response.status_code})"
            logger.info(f"[CHECK] {url} -> {status} | Latency: {duration_ms:.2f}ms")
            self.last_status[url] = {
                "status": status,
                "latency_ms": duration_ms,
                "timestamp": datetime.utcnow().isoformat(),
            }
            return status
        except requests.exceptions.RequestException as e:
            self.failure_count += 1
            logger.error(f"[FAIL] {url} -> Connection Error: {str(e)}")
            self.last_status[url] = {
                "status": "DOWN",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
            }
            return "DOWN"

    def run_loop(self):
        logger.info("🚀 Heartbeat Monitor Started. Polling every %ds", self.interval)
        while True:
            for endpoint in HEALTH_ENDPOINTS:
                status = self.check_health(endpoint)
                if self.failure_count >= self.alert_threshold:
                    logger.critical(
                        f"🚨 ALERT: Threshold breached ({self.failure_count} consecutive failures). Escalating to pilot cohort & ops."
                    )
            time.sleep(self.interval)


if __name__ == "__main__":
    monitor = UptimeMonitor(interval_seconds=30)
    monitor.run_loop()
