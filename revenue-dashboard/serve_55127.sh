#!/usr/bin/env bash
# Revenue Operations Console :55127 - deploy entrypoint (TASK-9AA3FC)
# DNA: MUST bind 0.0.0.0 (localhost bind trap drops external traffic).
set -euo pipefail
cd "$(dirname "$0")"
export HOST="${HOST:-0.0.0.0}"
export PORT="${PORT:-55127}"
exec python3 main.py
