# Art.12 Audit Log — SOW v2→Datasheet Consolidation Blocker: Publish-Flow Root-Cause Refinement (Code-Read Finding)

- **Date:** 2026-09-08 (UTC) · **Author:** GovernanceOfficer (Compliance Officer), nTrust.ai
- **Framework:** EU AI Act Art.12 (record-keeping) · NIST AI RMF (Govern/Map) · Core DNA Rule 5 (evidence-before-escalation)
- **Status:** Recorded — escalation supplemental to apr_cee35d2a (PENDING, Governor)

## 1. Context
- Canonical EAS SOW v2 ratification: `doc_af08c5ef44` v8 §12 (CEO Tier-3, 2026-09-08 ~22:20 UTC). Tiers UNCHANGED $15K/$35K/$50K · §4 40/40/20 HITL gates · §5 zero-trust + NIST AI RMF v1.0/2.0 + EU AI Act Art.9/12/14/15 + GDPR/CCPA · §7 ubazsec · §9 = nTrust.ai CEO · ubazsec · Client.
- **Consolidation target:** `doc_60c4005e77` (Datasheet record) — must absorb corrected SOW v2 onto the SAME doc object. **No standalone v2 fragment** (anti-fragmentation mandate).
- **Approved-but-unwired override:** `apr_498482c5` (Naveed, out-of-band) per board resolution `RAID-50507D`.
- **Blocker chain:** `RAID-51E28F` (4th reproduction) · `RAID-D0BADE` · `RAID-2AF8AB` · `RAID-84B69B` (→ TASK-27E190).

## 2. New Finding (Atlas, code-read — refines/supersedes guard-deploy-only hypothesis FOR THIS PATH)
1. `kb_fragmentation_guard_v2.py` (staged-not-deployed = TASK-27E190; 9/9 tests pass) **KEEPS "product" in DEDUPE_ACTIVE_CATEGORIES** → deploying guard v2 **alone will NOT unblock** the `doc_60c4005e77` consolidation.
2. **TRUE defect:** the `document_manager` publish flow treats **exact-title version updates as NEW fragments** — it does NOT perform a same-`doc_id` version bump BEFORE the anti-fragmentation guard evaluates. The guard therefore sees a would-be duplicate atomic fragment and rejects with the signature *"KB FRAGMENTATION DETECTED … Consolidation is Mandatory"* (identical to `doc_af08c5ef44` v8 §13).
3. Ready-to-publish consolidated content materialized on disk by Atlas: `ntrust/docs/sales-enablement/Datasheet_SOW_EAS_v2_consolidated_READY.md`.

## 3. Impact / State (verified)
- **NOT completed:** `doc_60c4005e77` not versioned to v2; corrected §4/§5/§7/§9 facts NOT yet written into target via `document_manager` (present only on disk + governance record v8 §12/§6).
- Defective v1 (`doc_3d7bd2e756`) already ARCHIVED/superseded — cannot circulate.
- No standalone v2 fragment created (guard prevented every publish attempt — integrity preserved).
- **Interim safety:** no client-facing issuance until persistence gate cleared.

## 4. Recommended Unblock Options (revised)
- **(c) DURABLE (revised recommendation):** owner **publish-flow fix** — exact-title publish must resolve to the same `doc_id` and execute a version bump BEFORE guard evaluation (guard skipped for same-`doc_id` version updates). Enforcement-layer code change ⇒ **EU AI Act Art.14 HITL: Board sign-off required via Nedo (CEO)**. No agent seat may self-authorize.
- **(a) INTERIM:** Governor **WriteTemp enforcement-layer override** to persist the consolidated record onto `doc_60c4005e77` now.
- **(b) guard v2 deployment (TASK-27E190):** NECESSARY for systemic KB-guard health but **NOT SUFFICIENT** for this consolidation path.

## 5. Evidence Chain
`RAID-51E28F` · TASK-27E190 · `doc_af08c5ef44` v8 §12/§6 · `apr_498482c5` (`RAID-50507D`) · Atlas artifact `Datasheet_SOW_EAS_v2_consolidated_READY.md` · PENDING L2: `apr_cee35d2a` + this supplemental.

*It is the numbers we trust.* 🔐📊 — GovernanceOfficer (Compliance Officer) · nTrust.ai
