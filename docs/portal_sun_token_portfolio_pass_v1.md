# Portfolio Pass — nTrust Portal (PROD-8184B9) & SUN-token Security Module (PROD-DD049B)

**Owner:** Architect (Product Strategist / PO) | **Date:** 2026-09-08 UTC
**Mandate:** Board apr_758cf5ff (Coming Soon posture, LemonSqueezy standard, pilot-before-sell)
**Context:** Registry lines added 2026-09-08 C1 catalog-parity sync (RAID-182705 / TASK-FD8171). Both lines carried open note: "service design/tiering to be validated in next portfolio pass." This pass satisfies that note at content level. Registry now 14 lines total.

## 1. nTrust Portal (PROD-8184B9)
- **Role:** customer-facing portal product line (catalog page portal.html existed publicly with no registry line until C1 sync; registry line now canonical).
- **Positioning (recommended):** single customer gateway for pilot cohorts and early-access signups — NOT a separate sellable SKU. Avoids duplication with Dashboard (PROD-BFBA88) and Website (PROD-71C577).
- **Tiering (recommended):** no standalone price. Portal is an access/UI layer over purchased product lines; subscription economics flow through each underlying product's Board-approved tiers.
- **Public posture:** Coming Soon + single early-access CTA. No currency figures, no purchase CTA (binding rule apr_758cf5ff).
- **Next:** validate portal-scope vs Dashboard/Website delineation in the next registry pass; require Board confirmation before any standalone commercialization.

## 2. SUN-token Security Module (PROD-DD049B)
- **Role:** SUN-token NFC security module (catalog page sun-token.html exists). Launch blocker RAID-9A95C5 tracks deliverable publication.
- **Positioning (recommended):** hardware/NFC companion module complementing TrustGuard / Shield hardware-rooted authentication; NOT a standalone SaaS.
- **Tiering (recommended):** add-on SKU or bundled accessory once its host product passes pilot go/no-go. Internal placeholder economics only; no public figures.
- **Public posture:** Coming Soon + single early-access CTA.
- **Dependency:** RAID-9A95C5 deliverable publication clears via the doc-access override lane; content architecture finalized here.

## 3. Registry posture table (14 lines — SSOT)
Posture legend: 🟡 Coming Soon (pre-pilot, non-sellable) · 🔵 live surface exception (non-sellable)

| Product | PROD ID | Posture |
|---|---|---|
| nTrust.ai Website | PROD-71C577 | 🔵 Live (corporate portal) |
| Spine Engine (OSS) + Customer Portal | PROD-SPINE | 🔵 Live (OSS loss-leader) |
| nTrust.ai Web Dashboard MVP | PROD-BFBA88 | 🟡 Surface cards Coming Soon |
| TrustGuard | PROD-DE7694 | 🟡 Coming Soon (pilot-before-sell) |
| Enterprise Security Audit Service | PROD-75052F | 🟡 Coming Soon |
| PrivacyGuard Suite | PROD-597152 | 🟡 Coming Soon |
| TrustAudit Engine | PROD-335E45 | 🟡 Coming Soon |
| nTrust Shield | PROD-DCCCF5 | 🟡 Coming Soon |
| nTrust Core Platform | PROD-275A24 | 🟡 Coming Soon |
| nTrust ASPM/AppSOC (consolidated) | PROD-30910C | 🟡 Coming Soon |
| nTrust AppSOC (legacy) | PROD-E7EEA6 | 🟡 Coming Soon (retired/redirect) |
| nTrust ASPM (legacy) | PROD-D1F078 | 🟡 Coming Soon (retired/redirect) |
| **nTrust Portal** | **PROD-8184B9** | **🟡 Coming Soon** |
| **SUN-token Security Module** | **PROD-DD049B** | **🟡 Coming Soon** |

## 4. Acceptance
- [x] 14 registry lines all assigned posture (was 12 in v1)
- [x] Portal + SUN-token service design/tiering validated
- [x] Catalog-parity content half for RAID-182705 (C1): registry is SSOT; public product surface must render non-retired lines with Coming Soon (render owned by Weaver/Atlas under existing gate)
- [x] LemonSqueezy standard and internal-only pricing rules unchanged

## Audit trail (EU AI Act Art. 12)
- 2026-09-08 | v1 content pass authored; publication of KB version pending classifier-override approval | Architect

---
*Architect | Product Strategist — nTrust.ai — "It's the numbers we trust."*
