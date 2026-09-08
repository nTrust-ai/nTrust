# PR #10 Fresh Ratification Evidence — Corrected Head 018d36ff

Generated: 2026-09-08T03:39:25.530440Z
Author: Atlas (Infrastructure & DevOps Director / Product Owner nTrust Shield)

## 1. Head confirmation

- Corrected head: `018d36ff68bbf2f534bef85a4d513a4a379280d4`
- Parent (superseded head): `5d25d2f3387a8665b8f0eda73518a4a4b7b6fe7b`
- Local ref `refs/heads/atlas/coming-soon-posture-ratified-2026-09-08` = 018d36ff (confirmed)
- Origin ref `refs/remotes/origin/atlas/coming-soon-posture-ratified-2026-09-08` = 018d36ff (pushed)
- Supersedes STALE records: `apr_code_cb36a8fd` + `apr_40461630` (both filed vs 5d25d2f3). Do NOT ratify; supersede.

## 2. Corrective commit scope (5d25d2f3 -> 018d36ff)

Files CHANGED by corrective commit: 7
- `frontend/dist/contact.html`
- `frontend/dist/products/enterprise-security-audit.html`
- `frontend/dist/products/managed-appsec.html`
- `frontend/dist/products/ntrust-core.html`
- `frontend/dist/products/portal.html`
- `frontend/dist/products/privacyguard.html`
- `frontend/dist/products/trustaudit.html`

Files UNCHANGED (zero drift, byte-identical parent->child): 9

## 3. Per-file sha256 @ 018d36ff (16-file PR scope)

| File | sha256 | Status |
|---|---|---|
| `frontend/dist/assets/site.css` | `d5702aa9da88d44b7a092984ffc884f26cabd679633947560074d745837e37ad` | unchanged |
| `frontend/dist/pricing.html` | `2bd7eed06de0b7dc47461392d4dea849416a49e86c7faf12340c0964b7f4daf8` | unchanged |
| `frontend/dist/about.html` | `41457b59155f985133b992fed0f599cb9135283405128ec930796503b5eb9e19` | unchanged |
| `frontend/dist/index.html` | `070d7d53ed49345521118d484ab6cd686c7d3878661678a4fae0bab763187589` | unchanged |
| `frontend/dist/contact.html` | `6e349cd5a4c820e2348b02d650e3e481511626fdd4c283f30728cd06c72e2953` | CHANGED (corrective) |
| `frontend/dist/pricing/index.html` | `0a5646145964dc0c74d7bee0767c92e3969669c6bf75d2d5290e8a5550293a26` | unchanged |
| `frontend/dist/products/index.html` | `2012e10e413f4dbee199c19c35656a384cbd0b6281fc605c49dc27a001745483` | unchanged |
| `frontend/dist/products/enterprise-security-audit.html` | `87413c7b339f357b13d297a6ce56bac554cde466c2c54c40c3c81591377656e2` | CHANGED (corrective) |
| `frontend/dist/products/managed-appsec.html` | `db59703f52d57de73fd58216ac59028454e4742eb05825696aa1be60bd05b22e` | CHANGED (corrective) |
| `frontend/dist/products/ntrust-core.html` | `4d2db7473fbdc44a62ad656b5f0b7f9d55f663c76b233c017a2329524787d77e` | CHANGED (corrective) |
| `frontend/dist/products/ntrust-shield.html` | `9c6378f47fadb90dafd8624e62f0145cf074312a87421eee3a35c69e8ed7e3d0` | unchanged |
| `frontend/dist/products/portal.html` | `dd219d26ff3b8c5415982986a3c8ab46b88cb8cf5a9c95bf3a842a6875d1074c` | CHANGED (corrective) |
| `frontend/dist/products/privacyguard.html` | `1625a352aa5ba4275fd44f1f84d5e9fa71d41785bac4880d5024cb862565f7e7` | CHANGED (corrective) |
| `frontend/dist/products/sun-token.html` | `b321e744cb859ca1558620a2472478cbc94c1aac9e7c7c41e1de6ac33e134617` | unchanged |
| `frontend/dist/products/trustaudit.html` | `bce2153b6eb4d2def9a143ac69f2c54b00dea1073cc20aa8481ea6c80f581b44` | CHANGED (corrective) |
| `frontend/dist/products/trustguard.html` | `818f4b2a9e9330a49dd42038b142b4e0927e29328aab8a8a21f6357dfc2be83a` | unchanged |

## 4. Gate-wording verification (7 corrective files)

Forbidden tokens (case-insensitive) across all 16 PR files:
- Talk to a Specialist = 0
- Start a Security Review = 0
- Available now / Available Now = 0
- Choose Starter|Growth|Enterprise = 0
- Request an Audit = 0
- Request a Consultation (order-intent band) = 0 on the 7 corrective files

Positive markers present on all 7 corrective files: 'Talk to an Expert' (nav), 'Coming Soon' badge, 'Join the Early-Access List'.

## 5. Transparent edge-case flag (out of scope, pre-existing)

- `frontend/dist/pricing/index.html` retains a lowercase 'Request a consultation' inside a 'Need a custom plan?' pricing CTA (link to /contact.html). This is PRE-EXISTING in origin/main 71f4c793 (verified), is NOT an order-intent 'Ready to get started' band, and is NOT part of the Coming-Soon product sweep. Flagged for Weaver's live-surface acceptance awareness.

## 6. Disposition

Awaiting Board (Naveed) one-click ratification of corrected head 018d36ff. No merge/deploy/closure before ratification. On ratification: merge PR #10 -> main -> deploy-sync :8085 docroot + Cloudflare Pages apex -> signal Weaver (gate fire #2).
