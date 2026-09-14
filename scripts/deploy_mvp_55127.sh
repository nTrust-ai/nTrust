#!/bin/bash
# Phase 3 MVP Redeployment Script - Port Binding Fix
# Binds development server to 0.0.0.0 for external access on Port 55127

echo "Stopping existing processes on port 55127..."
kill $(lsof -t -i:55127) 2>/dev/null || true

echo "Launching MVP server bound to 0.0.0.0:55127..."
python3 -m http.server 55127 --bind 0.0.0.0 &
SERVER_PID=$!

echo "Verifying external binding..."
lsof -i :55127 | grep LISTEN
if [ $? -eq 0 ]; then
    echo "✅ MVP successfully deployed to Port 55127 (0.0.0.0)"
else
    echo "❌ Deployment failed or port not responding"
fi

echo "Server PID: $SERVER_PID"