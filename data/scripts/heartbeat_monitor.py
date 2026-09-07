#!/usr/bin/env python3
"""
nTrust.ai Uptime Heartbeat Monitor
Phase 2: 24/7 Uptime Heartbeat & Error Logging Deployment

Monitors nTrust.ai infrastructure availability and logs status codes.
Compliant with NIST AI RMF guidelines for system transparency and availability.

Author: Architect (Product Strategist)
Date: 2026-06-25
"""

import urllib.request
import urllib.error
import datetime
import time
import logging
import os

# Configuration
MONITORED_ENDPOINTS = ["https://staging.ntrust.ai", "https://ntrust.ai"]
LOG_FILE = "/app/data/orgs/org_ntrust/data/logs/heartbeat_log.log"
CHECK_INTERVAL_SECONDS = 60  # Check every minute

# Setup logging
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def check_endpoint(url):
    """
    Perform HTTP health check on a given endpoint.

    Args:
        url (str): The URL to check

    Returns:
        tuple: (status_code, response_time_ms, error_message)
    """
    start_time = time.time()
    try:
        request = urllib.request.Request(
            url, headers={"User-Agent": "nTrust-Heartbeat/1.0"}
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            status_code = response.getcode()
            response_time_ms = int((time.time() - start_time) * 1000)
            return status_code, response_time_ms, None
    except urllib.error.HTTPError as e:
        response_time_ms = int((time.time() - start_time) * 1000)
        return e.code, response_time_ms, str(e)
    except urllib.error.URLError as e:
        response_time_ms = int((time.time() - start_time) * 1000)
        return None, response_time_ms, f"URL Error: {e.reason}"
    except Exception as e:
        response_time_ms = int((time.time() - start_time) * 1000)
        return None, response_time_ms, f"Unexpected error: {str(e)}"


def log_heartbeat():
    """
    Perform heartbeat check on all monitored endpoints and log results.
    """
    timestamp = datetime.datetime.utcnow().isoformat()
    logger.info(f"=== Heartbeat Check Started at {timestamp} ===")

    for endpoint in MONITORED_ENDPOINTS:
        status_code, response_time_ms, error = check_endpoint(endpoint)

        if error:
            logger.warning(
                f"CHECK FAILED: {endpoint} - {error} (Response Time: {response_time_ms}ms)"
            )
        else:
            status_level = "OK" if status_code == 200 else "WARNING"
            logger.info(
                f"{status_level}: {endpoint} - Status: {status_code} (Response Time: {response_time_ms}ms)"
            )

    logger.info("=== Heartbeat Check Complete ===\n")


def main():
    """
    Main loop for continuous uptime monitoring.
    """
    logger.info("Starting nTrust.ai Uptime Heartbeat Monitor")
    logger.info(f"Monitoring endpoints: {', '.join(MONITORED_ENDPOINTS)}")
    logger.info(f"Check interval: {CHECK_INTERVAL_SECONDS} seconds")

    while True:
        try:
            log_heartbeat()
            time.sleep(CHECK_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            logger.info("Heartbeat monitor stopped by user")
            break
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {str(e)}")
            time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
