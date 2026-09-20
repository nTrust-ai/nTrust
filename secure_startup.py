#!/usr/bin/env python3
"""nTrust.ai Secure Infrastructure Startup - Fixes directory listing vulnerability"""
import threading, time, sys, os

PORTS = {
    55004: "/app/data/server_55004.py",
    8085: "/app/data/secure_8085_server.py"
}

def start_server(port, filepath):
    """Start a server process for the given port"""
    if os.path.exists(filepath):
        import subprocess
        proc = subprocess.Popen(
            [sys.executable, filepath],
            stdout=open(f'/app/data/server_{port}.log', 'w'),
            stderr=subprocess.STDOUT
        )
        print(f"Started server on port {port} (PID: {proc.pid})")
    else:
        print(f"WARNING: File not found for port {port}: {filepath}")

if __name__ == "__main__":
    for port, filepath in PORTS.items():
        start_server(port, filepath)
    print("All secure servers initiated.")
