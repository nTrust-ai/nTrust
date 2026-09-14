#!/bin/bash
# TASK-5F1CF4 / TASK-140970: Bind Dev Servers to 0.0.0.0 for External Access
echo "🔧 Applying Port Binding Remediation..."

# Kill any existing localhost-bound dev servers
pkill -f "vite" || true
pkill -f "next dev" || true
pkill -f "python.*http.server" || true

# Restart Vite/Next.js with explicit 0.0.0.0 binding (Nginx/Cloudflare edge ready)
if [ -d "frontend" ] || [ -d "src" ]; then
  echo "✅ Starting frontend on 0.0.0.0:8085..."
  cd frontend && npm run dev -- --host 0.0.0.0 &
fi

if [ -f "app.py" ] || [ -f "main.py" ]; then
  echo "✅ Starting backend API on 0.0.0.0:55127..."
  python main.py --host 0.0.0.0 --port 55127 &
fi

echo "🚀 Infrastructure fix applied. External access enabled."
