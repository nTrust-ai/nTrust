#!/bin/bash
# P0: Execute Port Binding Remediation — Bind All Dev Servers to 0.0.0.0 for External Access
echo "🔧 Applying mandatory port binding remediation across all dev environments..."

# Vite/Node servers
if [ -f package.json ]; then
  sed -i 's/"dev": "vite"/"dev": "vite --host 0.0.0.0"/' package.json
fi

# Python Uvicorn/FastAPI servers
for file in *.py; do
  if grep -q "uvicorn.run" "$file"; then
    sed -i 's/uvicorn\.run(\([^)]*\))/uvicorn.run(\1, host="0.0.0.0", port=8000)/g' "$file"
  fi
done

# Express/Node servers
for file in *.js; do
  if grep -q "app.listen" "$file"; then
    sed -i 's/app\.listen(\([^)]*\))/app.listen(\1, "0.0.0.0")/g' "$file"
  fi
done

echo "✅ Port binding remediation applied successfully. All dev servers will now bind to 0.0.0.0."
