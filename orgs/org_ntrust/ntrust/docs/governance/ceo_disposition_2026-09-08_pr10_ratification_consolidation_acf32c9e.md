# CEO Disposition — PR #10 Merge Ratification Consolidation (2026-09-08)

## 1. Executive Summary
Live ntrust.ai violates `apr_758cf5ff` (Coming-Soon posture). Corrective action = merge PR #10.
Canonical head = `acf32c9e`. All `018d36ff`-based ratification requests are SUPERSEDED (incomplete posture).

## 2. Empirical Verification (CEO first-hand, 04:5x UTC)
- Screenshot + vision of https://ntrust.ai/products/: TrustGuard, Enterprise Security Audit, PrivacyGuard all render "Available now" (no "Coming Soon" badges); header CTA "Start a Security Review". VIOLATION CONFIRMED.
- PR #10 head SHA (git fetch origin): `acf32c9eba3a1f129f316aed0afea606dd724876` (branch `atlas/coming-soon-posture-ratified-2026-09-08`).
- Scope: 20 files, ALL under `frontend/dist/` (309 insertions / 173 deletions). No non-frontend artifacts.

## 3. SHA Discrepancy (root cause of duplicate filings)
- `5d25d2f3` — apr_code_cb36a8fd — REJECTED by Naveed ("route to the ceo").
- `018d36ff` — apr_8e13eb24 + apr_2fe0cefa — 2 commits BEHIND current head.
- `acf32c9e` — CURRENT mergeable head (CI-GREEN).

Delta `018d36ff -> acf32c9e` = EXACTLY 4 lines:
  frontend/dist/404.html, open-source/index.html, products/appsoc.html, products/aspm.html
  "Start a Security Review" -> "Talk to an Expert"  (zero order-intent CTAs site-wide)

## 4. Decision
- Canonical merge head = `acf32c9e`.
- `018d36ff` would leave 4 residual "Start a Security Review" CTAs = INCOMPLETE posture. REJECT.
- SUPERSEDE: apr_8e13eb24, apr_2fe0cefa, apr_code_cb36a8fd (already REJECTED), apr_40461630 (branch-ref resolves to acf32c9e but superseded for SHA pinning), apr_83672cdd (CEO's earlier gate, superseded by this consolidation).
- Single canonical path: Board ratification to merge PR #10 @ `acf32c9e`.

## 5. Staging DNS finding (Atlas, corroborated)
staging.ntrust.ai A-record = 127.0.0.1 (loopback) -> root cause of all "staging unreachable" reports.
Requires Cloudflare/DNS-owner (Naveed) fix to public origin. RAID logged separately.

## 6. Compliance
- EU AI Act Art.12: traceability via this record + AuditLog.
- Art.14 HITL: production merge routed to Naveed (human) for one-click sign-off. No self-approval.
