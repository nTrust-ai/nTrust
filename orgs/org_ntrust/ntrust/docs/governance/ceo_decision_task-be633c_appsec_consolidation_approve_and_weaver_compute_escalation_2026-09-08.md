# CEO Decision Record — TASK-BE633C (ASPM/AppSOC Consolidation) + Weaver Compute-Sandbox Escalation

Date: 2026-09-08 04:55 UTC
Author: Nedo (CEO, Tier-3)
Workstream: website-launch / product-strategy
Status: DECISION (APPROVE consolidation) + ESCALATION (Weaver compute restore)

## 1. Decision — TASK-BE633C Consolidation Routing: APPROVED

The Board REJECTED code promotion apr_code_7ddbfcd5 (TASK-BE633C) with feedback
"route to the ceo". Per that directive, the CEO has reviewed the promotion and
APPROVES the consolidation direction.

Promotion scope (presentation-only, sanitized):
- Reconcile legacy products/appsoc.html + products/aspm.html -> consolidated
  "nTrust ASPM/AppSOC — Coming Soon" managed offering (managed-appsec.html).
- Unify title/H1/breadcrumb; single Coming Soon badge; CTA -> "Join the Early
  Access List" (View Pricing removed); nav CTA -> "Talk to an Expert"; footer ->
  one consolidated link; SEO rel=canonical -> managed-appsec.html + noindex.
- Zero forbidden tokens, no credentials, no tier pricing surfaced (per Weaver).

Basis: Board apr_7a93177e (consolidation) + apr_758cf5ff (pre-pilot Coming Soon
posture). Sequencing satisfied: managed-appsec.html shipped in TASK-848C37 sweep
(apr_code_592e471c APPLIED).

## 2. CEO Empirical Verification (05:0x UTC, python3 stdlib)

- ntrust.ai/products/appsoc.html        -> HTTP 200 · 9237 B
- ntrust.ai/products/aspm.html          -> HTTP 200 · 9237 B
- ntrust.ai/products/managed-appsec.html-> HTTP 200 · 9237 B
  (all three byte-identical; "Coming Soon" x1, "Managed AppSec" x8,
   "Talk to an Expert" x1, no "View Pricing")
- ntrust.ai/products/                   -> HTTP 200 · 8014 B ("Coming Soon" x7,
   "View Pricing" x1 residual)

Finding: content consolidation is directionally correct and largely already live
on the individual product pages. Remaining delta = canonical/noindex SEO
consolidation + footer unification + removal of /products/ index "View Pricing"
residual.

## 3. Escalation — Weaver compute-sandbox restore (EU AI Act Art.14 HITL)

Weaver reports compute-sandbox detached ("Knowledge-Worker-only; bash denied").
Confirmed via docker_manager list: Weaver -> Env: None.

This blocks all remaining code work, including TASK-BE633C canonical/noindex
delta and TASK-848C37 Part-B pricing.html delta.

Precedent: Developer compute-sandbox restore required Board HITL (apr_af4e5f74,
Governor L2 RECOMMEND APPROVE; agent-side approval guardrail-blocked).

Note: env_c672eac2 ("Weaver-Acceptance-Exec-20260908") is provisioned but
currently assigned to Atlas. If it is a stale misassignment, reassignment to
Weaver may satisfy the compute requirement without a fresh provision.

## 4. Requested Board Action

(a) APPROVE Weaver compute-sandbox restore + non-live dev-surface write access
    (scope guards mirroring apr_af4e5f74): dynamic port sandbox, write confined
    to non-live dev surface (branch/sandbox copy), no C7/external-launch claim.
(b) Confirm consolidation approval is recorded (CEO APPROVE above is authoritative
    for the TASK-BE633C routing direction).

No self-approval, no self-merge. Awaiting Naveed (human Board) disposition.
