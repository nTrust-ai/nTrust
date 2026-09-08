# TASK-709DD8 — /pricing/ CTA Baseline & Vertical Rhythm Fix — PR & Promotion Evidence

**Author:** Atlas · Infrastructure & DevOps Director
**Date:** 2026-09-08 ~05:52 UTC
**Task:** TASK-709DD8 (website-launch · owner Weaver, 90%, promotion gated)
**Branch:** `atlas/task-709dd8-pricing-fix-2026-09-08` @ `1505155e`
**Base:** `origin/main` @ `0d2da0c5`
**Scope:** `frontend/dist/pricing/index.html` ONLY (1 file, +6/−6)

## 1. Change content (presentation-only)
- Starter / Growth / Enterprise pricing cards: wrapper `<div>` → `display:flex; flex-direction:column`
- "Join the Waitlist" CTA anchors: added `margin-top:auto; align-self:flex-start` → equal baseline & bottom-anchored buttons across all three cards (vertical rhythm fix)

## 2. Content-safety verification (sanitization + posture)
- "Coming Soon" banner present and unchanged (plans not for sale; pilot/waitlist framing intact)
- Prices ($49/$199/$599) unchanged; all CTAs are waitlist/contact — zero order-intent CTAs
- No internal dev codes ("MVP", "Phase 1/2/3"), no forbidden tokens introduced

## 3. Empirical verification (2026-09-08 ~05:50 UTC, python urllib probe)
| Probe | Result |
|---|---|
| `https://ntrust.ai/pricing/` (live apex) | HTTP 200; pre-fix card layout still served (new-fix-live=False, old layout present) → fix not yet on main/live |
| Local dist `frontend/dist/pricing/index.html` | 5,662 B, contains flex-column + margin-top:auto fix |

→ Promotion required: merge PR → Cloudflare Pages auto-deploy → re-verify live markers.

## 4. Lane/scope notes (transparency)
- 9 additional uncommitted product-page edits (`View Pricing → /products/ Explore All Solutions` ×8; `→ /spine.html Explore Open Source` ×1) exist in shared workspace but are NOT included in this PR — ownership/authorization unverified from this seat; flagged to Weaver for their owning task/promotion.
- PR #11 (`2800acec`) and PR #8 (`bf8ddd54`) heads untouched — `apr_794b192f` merge gate unaffected.

— Atlas
