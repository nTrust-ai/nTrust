# Publish-Flow Fix Spec — Same-doc_id Version Bump (TASK-999A22)

- **Date:** 2026-09-08 (UTC) · **Owner:** Atlas (Infrastructure & DevOps Director)
- **Gate:** EU AI Act Art.14 HITL — Board sign-off via Nedo (CEO) REQUIRED before deploy. No agent seat self-authorizes.
- **Predecessors:** RAID-51E28F · RAID-95E389 (root cause) · apr_498482c5 (approved override, unwired) · doc_60c4005e77 consolidation path.

## 1. Defect (confirmed, platform enforcement layer)
`document_manager` publish flow treats **exact-title version updates as NEW fragments**: no same-`doc_id` resolution and no version bump execute BEFORE the anti-fragmentation guard. The guard then sees a would-be duplicate atomic fragment and rejects with "KB FRAGMENTATION DETECTED … Consolidation is Mandatory."

## 2. Fix (enforcement-layer change to `document_manager` publish flow)
1. On publish, resolve **exact-title** (case/punctuation-normalized) against the existing KB registry.
2. If resolved → **reuse the existing `doc_id`** and execute a **version bump** on that same object (in-place update, not a new fragment).
3. **Skip the anti-fragmentation guard for same-`doc_id` version updates** (pass resolved `doc_id` so the guard's `e.doc_id == candidate.doc_id → continue` clause applies).
4. Keep the guard **active for genuinely NEW `doc_id`** publications (true fragment prevention).

## 3. Guard v2 compatibility (TASK-27E190)
`KbFragmentationGuardV2.is_duplicate_fragment()` already skips `e.doc_id == candidate.doc_id`. Once the publish flow resolves same-`doc_id`, guard v2 will NOT flag the version update. Guard v2 alone is NOT sufficient (it keeps "product" in DEDUPE_ACTIVE_CATEGORIES); the publish-flow resolution is the required companion.

## 4. Verification (to run post-deploy)
- Exact-title re-publish of `doc_60c4005e77` (SOW v2 consolidated content) resolves to existing `doc_id`, bumps version, no fragmentation rejection.
- New-title publish still guarded (fragment prevention intact).
- 9/9 guard v2 regression tests still pass (verified this turn: 9 passed, 0 failed).

*It is the numbers we trust.* 🔐 — Atlas · nTrust.ai
