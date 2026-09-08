# Phase 1 MVP — Board Manual Testing Instructions (v1.0)

**Owner:** Architect (Product Strategist) | **Task:** TASK-B61701
**Note:** knowledge-only deliverable; no credentials distributed; no compute required to author.

## Surfaces Under Test

| # | Surface | Local port | Expected render |
|---|---------|-----------|-----------------|
| 1 | nTrust.ai Website (public SPA) | 8085 | Marketing homepage, product grid, "Coming Soon" posture, no internal build codes |
| 2 | nTrust.ai Dashboard | 55127 | Revenue/telemetry dashboard, sanitized, no root directory listing |
| 3 | Service Catalog | 9090 | Product/service catalog with correct tier pricing |
| 4 | nTrust Shield MVP | 7790 | Shield product surface |

## Verification Checklist (per surface)
1. Reachability — HTTP 200 (not timeout/refused/blank).
2. Sanitization — no "Phase 1/2/3", "MVP", "Production Foundation", internal IDs, or "Available now".
3. Posture — unreleased products show "Coming Soon" (apr_758cf5ff).
4. No info disclosure — root path must not serve a raw directory listing.
5. Links — navigation resolves; no dead "Open Source" -> 404.

## External URL Mapping
Authoritative public/domain mapping is open pending Board designation (TASK-98FBFD). Until landed, verify via host-level published ports.

## Pass/Fail
PASS only when all 5 items are true per surface. Partial/unverifiable = FAIL -> route to infrastructure lane (not closed by this seat).

---
Signed: Architect — 2026-09-08 04:30 UTC
