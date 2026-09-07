#!/usr/bin/env python3
import socket
import urllib.request
import ssl
import sys


def diagnose_staging():
    host = "staging.ntrust.ai"
    port = 443
    results = []

    # 1. DNS Resolution Check
    try:
        ip = socket.gethostbyname(host)
        results.append(f"✅ DNS RESOLVED: {host} -> {ip}")
    except socket.gaierror as e:
        results.append(f"❌ DNS FAILED: {host} - {e}")
        print("\n".join(results))
        return

    # 2. HTTPS Connectivity Check
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(f"https://{host}/", method="HEAD")
        response = urllib.request.urlopen(req, context=context, timeout=10)
        results.append(f"✅ HTTPS CONNECTED: Status {response.status}")
    except urllib.error.URLError as e:
        results.append(f"❌ HTTPS FAILED: {e.reason}")
    except Exception as e:
        results.append(f"❌ ERROR: {e}")

    print("\n".join(results))


if __name__ == "__main__":
    diagnose_staging()
