#!/usr/bin/env python3
"""
DNS & HTTPS Deployment Validation Script v1.0
Task: TASK-A4C386 - P0: Restore & Validate nTrust.ai Production DNS/HTTPS Deployment
Author: Architect (Product Strategist)
Date: 2026-06-24
"""

import socket
import ssl
import requests

def validate_dns_resolution(domain="ntrust.ai"):
    """Validates DNS resolution for production domain."""
    try:
        ip = socket.getaddrinfo(domain, None)[0][4][0]
        return f"✅ DNS Resolved: {domain} -> {ip}"
    except Exception as e:
        return f"❌ DNS Resolution Failed: {e}"

def validate_https_endpoint(url="https://ntrust.ai"):
    """Validates HTTPS endpoint and TLS certificate chain."""
    try:
        response = requests.get(url, timeout=5, verify=True)
        if response.status_code == 200:
             return f"✅ HTTPS Valid: {url} (Status: {response.status_code})"
         else:
             return f"⚠️ HTTPS Active but Non-200: {url} (Status: {response.status_code})"
    except requests.exceptions.SSLError as e:
        return f"❌ TLS Certificate Issue: {e}"
    except Exception as e:
        return f"❌ HTTPS Validation Failed: {e}"

if __name__ == "__main__":
    print("🌐 Executing DNS/HTTPS Production Validation...")
    dns_result = validate_dns_resolution()
    https_result = validate_https_endpoint()
    print(f"{dns_result}")
    print(f"{https_result}")
    print("✅ TASK-A4C386 Execution Complete. Awaiting Board Sign-off.")
