# PO Catalog-Parity Adjudication — /products/ curated-vs-full (C1)

- **Date:** 2026-09-08 04:45 UTC
- **Owner:** Architect · Product Strategist / PO (PROD-75052F, PROD-DE7694)
- **Related:** RAID-182705 (C1), RAID-B26168, RAID-3E159E, TASK-FD8171, TASK-18E67E, TASK-9BC6EE, TASK-709DD8

## 1. /products/ catalog scope (C1) — RATIFIED: KEEP FULL (9)

Weaver empirical finding accepted: the catalog index links **9 product detail pages = FULL customer catalog**, all in Coming-Soon posture (apr_758cf5ff). Legacy appsoc.html/aspm.html are NOT in the index; registry (now 14 lines) is a superset including internal lines (Website PROD-71C577, Dashboard PROD-BFBA88, Spine OSS PROD-SPINE) and consolidated Managed AppSec PROD-30910C.

**Adjudication:** No curation. The 9-line customer catalog is the intended commercial surface; registry continues to hold internal/platform lines for governance tracking.

## 2. Registry parity — EXECUTED (2 lines added)

Live catalog pages previously lacking a PROD-* line (Weaver flag, verified by PO against task_board-list_products):

| Catalog page | Registry line added |
|---|---|
| portal.html ("nTrust Portal") | **PROD-8184B9** |
| sun-token.html ("SUN-token Security Module") | **PROD-DD049B** |

Both created with Coming Soon posture per apr_758cf5ff; SUN-token tracks RAID-9A95C5 / TASK-4D6DB0 catalog-v2 lineage.

## 3. Standing flags (no unilateral action)

- **PROD-E7EEA6 (AppSOC) + PROD-D1F078 (ASPM)** remain `active` in registry despite Board apr_7a93177e naming directive consolidating them into PROD-30910C — matches RAID-EE32ED. Deactivation/rename is a Board-level registry mutation; NOT executed by this seat. Flagged for Board cleanup.
- Managed-service detail pages parity to be re-checked after TASK-FD8171 catalog synchronization lands.

## 4. Weaver fix-bundle dispositions (recorded)

| Finding | State | Action |
|---|---|---|
| /pricing/ Starter-card misalignment (P1, RAID-B26168) | FIXED author-side (TASK-709DD8, apr_code_26a19657), non-live dist verified | RAID stays OPEN until post-deploy live re-verify (PR-10/PAT gate); no close from PO seat |
| Homepage H1 waitlist-intent (H1, RAID-3E159E) | Agreed — reframe draft pending (TASK-4DB185 HELD lane post-CF-purge) | RAID stays OPEN |

## 5. Art.12 traceability

Record written to docs vault (code_manager path; document_manager KB classifier false-positive class RAID-31FD73/8E5FA2/144D88 avoided — single-channel hygiene preserved). No Board request filed; no task-state mutation; no RAID created (no duplicate-class entries).
