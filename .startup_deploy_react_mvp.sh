#!/bin/bash
# Atlas — Auto-deploy React MVP to prod/www on container startup
# Ensures port 8085 always serves the latest React build
if [ -d /app/data/frontend/dist ]; then
    mkdir -p /app/data/prod/www
    cp -r /app/data/frontend/dist/* /app/data/prod/www/
    echo "[Atlas] React MVP deployed to /app/data/prod/www/ on startup"
else
    echo "[Atlas] WARNING: frontend/dist not found, building..."
    cd /app/data/frontend && npx vite build 2>&1
    mkdir -p /app/data/prod/www
    cp -r /app/data/frontend/dist/* /app/data/prod/www/
    echo "[Atlas] React MVP built and deployed on startup"
fi
