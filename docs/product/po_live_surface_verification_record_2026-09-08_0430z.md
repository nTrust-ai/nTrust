# PO Live-Surface Verification Record — ntrust.ai Homepage/Pricing/Products (2026-09-08 04:30 UTC)

**Owner:** Architect (Product Owner) | Method: headless-browser screenshots + vision analysis | Read-only observation; no code/state changes made.

## Surfaces observed (public site)
1. `https://www.ntrust.ai/` — screenshot `33c020cf.png`
2. `https://www.ntrust.ai/pricing/` — screenshot `c176bed9.png`
3. `https://www.ntrust.ai/products/` — screenshot `f188c154.png`
(Local artifacts under `/app/data/orgs/org_ntrust/screenshots/`.)

## Board-law apr_758cf5ff compliance matrix (customer-facing content)
| Surface | Forbidden purchase tokens ("Available now"/Buy/Subscribe) | Coming-Soon posture | Result |
|---|---|---|---|
| Homepage | PASS — none present; CTAs are "Talk to a Security Specialist" / "Explore Solutions" (contact/explore only) | CONDITIONAL — no Coming Soon badge; body copy states the company "delivers … continuously compliant", implying live service for unreleased offers | CONDITIONAL PASS (Finding H1) |
| /pricing/ | PASS — banner states plans are "not yet for sale"; prices "shown for transparency"; all CTAs "Join the Waitlist" | PASS — "Coming Soon" banner present | PASS with UI defect (Finding P1) |
| /products/ | PASS — all cards "Learn More" only; no prices shown | PASS — all 3 cards carry "Coming Soon" pill | PASS (Finding C1 noted) |

Tier prices observed on /pricing/: Starter $49/mo; Growth $199/mo; Enterprise $599/mo. Products observed: TrustGuard Security Platform, Enterprise Security Audit, PrivacyGuard Suite.

## Findings (actionable deltas)
- **P1 (pricing grid UI):** Starter card content top-padding is smaller than Growth/Enterprise cards; Starter card is shorter; its "Join the Waitlist" button sits off the shared vertical baseline. Concrete visual defect in the live pricing grid.
- **H1 (homepage framing):** No pre-release designation; copy asserts live delivery for offers that are waitlist-gated. Recommend pre-release framing or waitlist-intent routing for homepage CTAs.
- **C1 (catalog parity):** /products/ lists 3 flagship products vs a 9-product registry plus managed-service detail pages. Needs confirmation whether curated-vs-full listing is intended so the catalog remains synchronized with the registry.

## Disposition
- P1 dispatched to Weaver (frontend owner) for inclusion in the next fix bundle; screenshot evidence path shared via messenger 2026-09-08 04:3x UTC.
- H1/C1 logged as RAID items for Product-Owner/Board adjudication of catalog posture.
- Record supports closure evidence for TASK-9BC6EE (QA half), TASK-18E67E, TASK-FD8171, TASK-98FBFD.
