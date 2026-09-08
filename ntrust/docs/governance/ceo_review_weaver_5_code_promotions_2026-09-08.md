# CEO Review & Recommendation — Weaver's 5 P1 Frontend Code Promotions

**Reviewer:** Nedo (CEO · exclusive Board Delegate)
**Date:** 2026-09-08 07:45 UTC
**Requestor:** Weaver (PO, website-launch)
**Workstream:** website-launch
**Promotion IDs:** apr_code_5b59d6a9 · apr_code_1339b27d · apr_code_26a19657 · apr_code_5f51feb7 · apr_code_b4534c2b

## VERDICT: RECOMMEND APPROVE — all 5 (no defects found)

## 1. Scope & mapping (CEO independent verification)

| # | Weaver label | Concrete change | Empirical basis |
|---|---|---|---|
| 1 | CSS edge-cache root-cause | PR #11 sync `orgs/org_ntrust/abtest/assets/site.css` → canonical | sha1/wc reconciled below |
| 2 | homepage hero copy | `index.html` early-access badge + waitlist CTA | diff inspected |
| 3 | /pricing/ Starter baseline | PR #12 (TASK-709DD8) flex-column + margin-top:auto | diff + file size |
| 4 | ASPM/AppSOC reconciliation | footer `nTrust ASPM`+`nTrust AppSOC` → `Managed AppSec Services` | diff inspected |
| 5 | pre-pilot "View Pricing" sweep | 9 product pages "View Pricing" → "Explore All Solutions"/"Explore Open Source" | diff inspected |

## 2. Customer-facing sanitization — PASS (EU AI Act Art.12 / mission §C3)
- **Zero internal dev codes:** `MVP` / `Phase 1|2|3` → 0 hits across staged dist.
- **"Coming Soon" designations intact** on `/pricing/` + `managed-appsec.html` (unreleased-products rule).
- **Waitlist-only CTAs:** pricing page = 3× "Join the Waitlist"; zero order-intent tokens (View Pricing/Buy/Purchase/Checkout).
- **No 404s:** all changed href targets exist on disk — `/spine.html`, `/products/managed-appsec.html`, `/pricing/index.html`, `/products/index.html`, `/contact.html`.

## 3. CSS edge-cache root-cause — AUTHORITATIVE (reconciled this cycle)
- **Canonical** `frontend/dist/assets/site.css` = **11,797 B · sha1 `8751c9f6c5378bfc0f2e4679706beddfc843f6d8` · 6× text-wrap**
- **Stale docroot** `orgs/org_ntrust/abtest/assets/site.css` = **10,995 B · sha1 `feb4ff7cd40c6c351273b36d6fe29582368fd9e8` · 0× text-wrap**
- **`_headers` /assets/*** already reconciled on main (`0d2da0c5`): `immutable` removed → `max-age=3600, stale-while-revalidate=86400`.
- PR #11 is the correct docroot→canonical sync; this is the true root-cause fix (cache purge alone would re-serve stale bytes).

## 4. Dependency note (post-approval, non-blocking for this gate)
CF cache purge (`apr_6f855f72` + 3 siblings — **APPROVED, unexecuted**) must still land for the edge to flip from `feb4ff7cd40c` → `8751c9f6c537`. Code promotion + merge is necessary but not sufficient.

## 5. Recommendation to Board
Approve all 5 code promotions; authorize CEO merge execution on Naveed approval; then execute the standing CF purge to close TASK-4DB185 + TASK-AF07D1 D1/D6.

— Nedo · CEO · nTrust.ai · "It's the numbers we trust."
