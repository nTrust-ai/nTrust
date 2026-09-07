import time
import logging
import requests
from datetime import datetime
import os

# Configuration & Constants
TARGET_URL = "http://staging.ntrust.ai"
CHECK_INTERVAL_SECONDS = 60
LOG_DIR = "/app/data/orgs/org_ntrust/uptime_logs"
LOG_FILE = f"{LOG_DIR}/heartbeat.log"


def setup_logging():
    """Initialize structured file-based logging for uptime tracking."""
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def check_uptime():
    """Core Heartbeat Logic: Validates service availability & logs status/errors."""
    try:
        response = requests.get(TARGET_URL, timeout=10)
        if response.status_code == 200:
            logging.info(f"HEALTHY: Service {TARGET_URL} is UP (Status: 200).")
        else:
            logging.warning(
                f"DEGRADED: Service {TARGET_URL} status is {response.status_code}. Retrying next cycle."
            )
    except requests.exceptions.RequestException as e:
        logging.error(f"CRITICAL FAILURE: Service {TARGET_URL} is DOWN. Error: {e}")


if __name__ == "__main__":
    setup_logging()
    logging.info("Heartbeat Monitor initialized. Starting periodic health checks...")
    while True:
        check_uptime()
        time.sleep(CHECK_INTERVAL_SECONDS)
