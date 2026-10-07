#!/usr/bin/env bash
# TrustBrain™ one-line installer (Pillar 2 — trustbrain.ntrust.ai/install.sh)
# Idempotent. Deploys the sovereign reasoning engine as a standalone OCI container (port 8092).
# No telemetry egress. Data stays on your infrastructure.
set -euo pipefail

TRUSTBRAIN_REPO="${TRUSTBRAIN_REPO:-https://github.com/ntrustai/trustbrain.git}"
TRUSTBRAIN_VERSION="${TRUSTBRAIN_VERSION:-main}"
TRUSTBRAIN_PORT="${TRUSTBRAIN_PORT:-8092}"
INSTALL_DIR="${TRUSTBRAIN_INSTALL_DIR:-$HOME/.ntrust/trustbrain}"
COMPOSE_PROJECT="trustbrain"

log()  { printf '\033[1;36m[trustbrain]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[trustbrain]\033[0m %s\n' "$*"; }
die()  { printf '\033[1;31m[trustbrain] ERROR: %s\033[0m\n' "$*" >&2; exit 1; }

need() { command -v "$1" >/dev/null 2>&1 || die "missing dependency: $1 (install it first)"; }

usage() { cat <<'USG'
Usage:
  curl -fsSL https://trustbrain.ntrust.ai/install.sh | bash
  bash install.sh --uninstall      # stop and remove the TrustBrain engine

Environment variables:
  TRUSTBRAIN_REPO     Git repo of the engine (default: ntrustai/trustbrain)
  TRUSTBRAIN_VERSION  Branch/tag to install (default: main)
  TRUSTBRAIN_PORT     Host port to bind (default: 8092)
  TRUSTBRAIN_INSTALL_DIR  Install directory (default: ~/.ntrust/trustbrain)
USG
}

case "${1:-}" in
  -h|--help) usage; exit 0 ;;
esac

if [ "${1:-}" = "--uninstall" ]; then
  log "Uninstalling TrustBrain…"
  if [ -d "$INSTALL_DIR" ]; then
    (cd "$INSTALL_DIR" && docker compose -p "$COMPOSE_PROJECT" down --remove-orphans 2>/dev/null || true)
    rm -rf "$INSTALL_DIR"
  fi
  docker rm -f trustbrain 2>/dev/null || true
  log "TrustBrain removed."
  exit 0
fi

need git
need docker

if docker compose version >/dev/null 2>&1; then COMPOSE="docker compose"; else
  need docker-compose; COMPOSE="docker-compose"; fi

log "Installing TrustBrain™ (repo=$TRUSTBRAIN_REPO version=$TRUSTBRAIN_VERSION port=$TRUSTBRAIN_PORT)"

if [ -d "$INSTALL_DIR/.git" ]; then
  log "Existing install found at $INSTALL_DIR — pulling latest…"
  (cd "$INSTALL_DIR" && git fetch --depth 1 origin "$TRUSTBRAIN_VERSION" && git checkout -f "$TRUSTBRAIN_VERSION")
else
  log "Cloning engine into $INSTALL_DIR…"
  mkdir -p "$INSTALL_DIR"
  git clone --depth 1 --branch "$TRUSTBRAIN_VERSION" "$TRUSTBRAIN_REPO" "$INSTALL_DIR"
fi

if [ -f "$INSTALL_DIR/Dockerfile" ] || [ -f "$INSTALL_DIR/docker-compose.yml" ]; then
  log "Starting engine on 0.0.0.0:$TRUSTBRAIN_PORT…"
  TRUSTBRAIN_PORT="$TRUSTBRAIN_PORT" "$COMPOSE" -p "$COMPOSE_PROJECT" -f "$INSTALL_DIR/docker-compose.yml" up -d --build 2>/dev/null \
    || TRUSTBRAIN_PORT="$TRUSTBRAIN_PORT" "$COMPOSE" -p "$COMPOSE_PROJECT" up -d
else
  log "No container manifest found — running engine via Python runtime…"
  need python3
  (cd "$INSTALL_DIR" && python3 -m pip install -q -r requirements.txt && \
     nohup uvicorn main:app --host 0.0.0.0 --port "$TRUSTBRAIN_PORT" >/tmp/trustbrain.log 2>&1 &)
fi

log "Waiting for health endpoint…"
for i in $(seq 1 30); do
  if command -v curl >/dev/null 2>&1 && curl -fsS "http://localhost:$TRUSTBRAIN_PORT/api/v1/health" >/dev/null 2>&1; then
    log "✅ TrustBrain™ is live at http://localhost:$TRUSTBRAIN_PORT"
    log "Health: http://localhost:$TRUSTBRAIN_PORT/api/v1/health"
    exit 0
  fi
  sleep 1
done
warn "Engine may still be starting — check logs and retry the health endpoint."
exit 0
