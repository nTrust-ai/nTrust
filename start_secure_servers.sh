#!/bin/bash
cd /app/data

# Kill any existing insecure servers
pkill -f "SimpleHTTPRequestHandler" 2>/dev/null || true
sleep 1

# Start server on port 55004 (secure, no directory listing)
python3 server_55004.py &
echo "Started 55004"

# Start server on port 8085 (secure MVP)
python3 secure_8085_server.py &
echo "Started 8085"

wait
