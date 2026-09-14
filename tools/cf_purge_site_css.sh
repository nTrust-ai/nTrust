#!/usr/bin/env bash
# =============================================================================
# tools/cf_purge_site_css.sh — One-shot Cloudflare purge + live re-verify
# Owner : Weaver (Lead Frontend & UI Engineer)
# Scope : TASK-4DB185 residual — edge-stale https://ntrust.ai/assets/site.css
#         (immutable max-age=31536000 blocking the Board-visible D1-D6 CSS fix)
# Deps  : curl (+ python3 or jq for API response parsing)
#
# Zero-trust: NO credentials embedded. Reads from environment only.
#   export CLOUDFLARE_API_TOKEN="<provisioned token>"   (Zone.Cache Purge perm)
#   export CF_ZONE_ID="<zone id>"
#   bash tools/cf_purge_site_css.sh            # purge + verify (one-shot)
#   bash tools/cf_purge_site_css.sh verify     # verify only (e.g. after an
#                                              #  owner one-click "Purge Everything")
#
# Exit codes: 0 = green (purge applied + live CSS carries fix markers)
#             2 = missing env vars      3 = Cloudflare API failure
#             4 = verification failure (edge still stale)
# =============================================================================
set -euo pipefail

ZONE_ID="${CF_ZONE_ID:-}"
API_TOKEN="${CLOUDFLARE_API_TOKEN:-}"
API_BASE="https://api.cloudflare.com/client/v4"
ASSET_URL="https://ntrust.ai/assets/site.css"

# Canonical fix markers that MUST be present in the live (edge) CSS after purge.
# Derived from frontend/dist/assets/site.css (canonical, apr_code_292ea15a):
#   D-orphan/rag : text-wrap:balance on .hero h1 + .sec-title
#   D-responsive : nav wrap @max-width:980px (mobile nav no longer hidden)
#   D-card-cta   : bottom-anchored card CTA (.card-cta / price-card .btn)
MARKERS=("text-wrap:balance" "@media(max-width:980px)" ".card-cta{margin-top:12px;text-align:center;width:100%;}")

log()  { printf '[cf-purge] %s\n' "$*"; }
die()  { printf '[cf-purge] ERROR: %s\n' "$*" >&2; exit "${2:-1}"; }

# ------------------------------------------------------------------ verify fns
verify_edge() {
  local body headers http ok=1
  log "Verifying edge copy of ${ASSET_URL} ..."
  headers="$(mktemp)"; body="$(mktemp)"
  http="$(curl -sS -o "$body" -D "$headers" -w '%{http_code}' \
        -H 'Accept: text/css,*/*' "$ASSET_URL" || true)"

  if [ "$http" != "200" ]; then
    log "HTTP ${http} from edge (expected 200)."
    ok=0
  else
    grep -qi 'cf-cache-status' "$headers" && { log "Headers: $(grep -i 'cf-cache-status' "$headers" | tr -d '\r')"; }
    for m in "${MARKERS[@]}"; do
      if grep -qF -- "$m" "$body"; then
        log "  marker OK   : ${m}"
      else
        log "  marker MISS : ${m}"
        ok=0
      fi
    done
  fi
  rm -f "$headers" "$body"
  return $ok
}

# --------------------------------------------------------------------- main
if [ "${1:-}" = "verify" ]; then
  verify_edge && { log "GREEN: edge CSS is canonical (D1-D6 fix is board-visible)."; exit 0; }
  die "Edge CSS is STILL STALE (missing canonical markers). Re-check purge." 4
fi

[ -n "$ZONE_ID" ]  || die "CF_ZONE_ID not set. Aborting (zero-trust)." 2
[ -n "$API_TOKEN" ] || die "CLOUDFLARE_API_TOKEN not set. Aborting (zero-trust)." 2

log "Targeted purge: ${ASSET_URL} (zone ${ZONE_ID})"
resp="$(curl -sS -X POST "${API_BASE}/zones/${ZONE_ID}/purge_cache" \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data "{\"files\":[\"${ASSET_URL}\"]}")"

# Parse success flag (python3 fallback if jq absent)
if command -v jq >/dev/null 2>&1; then
  ok="$(printf '%s' "$resp" | jq -r '.success // false')"
  errs="$(printf '%s' "$resp" | jq -r '[.errors[]?.message] | join("; ")')"
else
  ok="$(printf '%s' "$resp" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(str(d.get("success",False)).lower())' 2>/dev/null || echo false)"
  errs="$(printf '%s' "$resp" | python3 -c 'import sys,json;d=json.load(sys.stdin);print("; ".join(e.get("message","") for e in d.get("errors",[])))' 2>/dev/null || true)"
fi

if [ "$ok" != "true" ]; then
  die "Cloudflare purge rejected: ${errs:-$(printf '%s' "$resp" | head -c 500)}" 3
fi
log "Purge API accepted (success=true). Waiting 6s for edge propagation ..."
sleep 6

verify_edge && { log "GREEN: purge applied; edge CSS is canonical. D1-D6 re-verify (desktop + 375px) can proceed."; exit 0; }
die "Purge accepted but edge verification FAILED. Retry once; if persistent, re-check zone/token scope." 4
