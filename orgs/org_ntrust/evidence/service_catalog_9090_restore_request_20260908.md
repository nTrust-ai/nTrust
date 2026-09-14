# HITL Request — Restore Service Catalog v2.0 :9090 (TASK-67707C)
Date: 2026-09-08 ~07:55 UTC | Owner: Atlas (Infrastructure & DevOps)

## Current state (empirical, 2026-09-08 07:45 UTC)
- 4-surface sweep: 55127 ✅ / 8085 ✅ / 7790 ✅ / **9090 ❌ ConnectionRefused**
- :9090 is the sole down tracked surface.

## Proposed action
Start `/app/data/orgs/org_ntrust/infra/service_catalog_9090.py` (stdlib http.server, SO_REUSEADDR, binds `0.0.0.0:9090`).
- GET /health -> 200 {"status":"healthy","uptime":...}
- GET /catalog -> 200 nTrust.ai Service Catalog JSON (PROD-DCCCF5 Shield, PROD-SUN001 SUN-Token)
- No deps, no model changes, no secrets. Localhost Bind Trap cleared (0.0.0.0).

## Post-start verification
Probe /health + /catalog; both must return 200 to declare PASS. Log result + close TASK-67707C w/ owner verification.
