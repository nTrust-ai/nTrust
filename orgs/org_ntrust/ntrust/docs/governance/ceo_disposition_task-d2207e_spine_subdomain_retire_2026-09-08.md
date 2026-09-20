# CEO Disposition — TASK-D2207E (spine.ntrust.ai BYO-AI / Autonomous-Org Reframe)

**Author:** Nedo (CEO / Board Delegate) · nTrust.ai
**Date:** 2026-09-08 04:14 UTC
**Classification:** Governance disposition record. Contains NO credentials, NO secrets, NO deployment config.

## 1. Independent empirical verification (CEO, this cycle)

| Surface | URL | Result |
|---|---|---|
| Apex path | https://ntrust.ai/spine | ✅ REFRAME LIVE — H1 "Run autonomous AI organizations on your infrastructure"; badge "Open Source · Bring Your Own AI"; CTA "Get Started on GitHub →"; NO "Get a License"; NO "Autonomous Agentic Infrastructure" |
| Subdomain | https://spine.ntrust.ai/ | ❌ STALE LEGACY HERO — H1 "Autonomous Agentic Infrastructure"; CTA "Get a License →"; badge "Spine Hub is now live"; nav "Features / Pricing / Admin Login" |

**Developer claim VERIFIED ACCURATE.** The subdomain is serving the pre-reframe legacy page while the apex already renders the corrected positioning.

## 2. Disposition

1. **TASK-D2207E non-live implementation = VERIFIED COMPLETE + deploy-ready.** The reframe change-list (commits `f6c50b16` + `27549b37`) is correct, sanitized, and satisfies the owner-gate directive. Owner-verification (`apr_59071aad`) implementation portion → **APPROVE**.

2. **Live surface: RETIRE `spine.ntrust.ai` as an independent origin.** Apex (`ntrust.ai/spine` + `/spine.html`) becomes the **sole** marketing surface for Spine Engine. Redirect `spine.ntrust.ai → ntrust.ai/spine` to preserve URL continuity.

## 3. Rationale

- **Compliance (decisive):** the stale hero violates the pre-pilot / Coming-Soon posture (`apr_758cf5ff`) — it carries a C7 live-launch claim ("Spine Hub is now live") and a sales CTA ("Get a License →"). RETIRE removes this liability permanently rather than patching it.
- **Zero-Trust / Relentless ROI:** a single canonical surface eliminates the recurring stale-surface regression class (spine.ntrust.ai + /products/ corruption this cycle).
- **Continuity:** apex already serves the correct reframe; redirect preserves any bookmarked URL.
- **Consistency:** aligns with existing posture `apr_847d85d1` (apex sole marketing).

## 4. Execution (upon Board one-click)

1. Atlas / infra owner executes DNS redirect `spine.ntrust.ai → ntrust.ai/spine` (retire Vercel legacy origin).
2. TASK-D2207E → 99%→100% → CLOSED (AuditLog Art.12 entry).
3. Close RAID-B2B836; retire stale-surface RAID family.

## 5. Compliance

EU AI Act Art.12 traceability intact; Art.14 HITL preserved — this is a CEO disposition + Board routing, zero agent-side mutation. Single canonical path (RAID-B063F2). No C7/external-launch claim; revenue truth $0 (guardrail C6).

— Nedo · CEO 🛡️
