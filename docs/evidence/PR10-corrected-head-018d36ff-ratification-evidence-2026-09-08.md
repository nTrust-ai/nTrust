# PR #10 Corrected Head — Ratification Evidence (018d36ff)

**Date:** 2026-09-08 03:27 UTC
**Author:** Atlas (Infrastructure & DevOps Director / Product Owner nTrust Shield)
**Lane:** website-launch · TASK-4A4179 / TASK-4DB185 / TASK-848C37
**Supersedes:** apr_code_cb36a8fd + apr_40461630 (both filed against superseded head 5d25d2f3 — DO NOT ratify)

## 1. Reference objects
| Object | Value |
|---|---|
| Branch / PR | `atlas/coming-soon-posture-ratified-2026-09-08` → **PR #10** |
| Corrected head | `018d36ff68bbf2f534bef85a4d513a4a379280d4` |
| Prior (superseded) head | `5d25d2f3` |
| Base (origin/main) | `71f4c7932d212063609c7efc0a2283cf73ed6d5d` |

## 2. Canonical-owner sign-off
Weaver (Lead Frontend & UI Engineer, canonical copy owner) SIGNED OFF `018d36ff` = GREEN vs frozen canonical wording (doc_74d6a48d9b §3 / doc_f970c2179f §2). Binding acceptance remains Weaver's live-surface post-deploy scan.

## 3. Per-file sha256 @ 018d36ff (13 canonical files) — 13/13 PASS
| File (frontend/dist/) | sha256 |
|---|---|
| index.html | 070d7d53ed49345521118d484ab6cd686c7d3878661678a4fae0bab763187589 |
| products/index.html | 2012e10e413f4dbee199c19c35656a384cbd0b6281fc605c49dc27a001745483 |
| pricing.html | 2bd7eed06de0b7dc47461392d4dea849416a49e86c7faf12340c0964b7f4daf8 |
| about.html | 41457b59155f985133b992fed0f599cb9135283405128ec930796503b5eb9e19 |
| products/trustguard.html | 818f4b2a9e9330a49dd42038b142b4e0927e29328aab8a8a21f6357dfc2be83a |
| products/ntrust-shield.html | 9c6378f47fadb90dafd8624e62f0145cf074312a87421eee3a35c69e8ed7e3d0 |
| products/sun-token.html | b321e744cb859ca1558620a2472478cbc94c1aac9e7c7c41e1de6ac33e134617 |
| products/enterprise-security-audit.html | 87413c7b339f357b13d297a6ce56bac554cde466c2c54c40c3c81591377656e2 |
| products/privacyguard.html | 1625a352aa5ba4275fd44f1f84d5e9fa71d41785bac4880d5024cb862565f7e7 |
| products/trustaudit.html | bce2153b6eb4d2def9a143ac69f2c54b00dea1073cc20aa8481ea6c80f581b44 |
| products/managed-appsec.html | db59703f52d57de73fd58216ac59028454e4742eb05825696aa1be60bd05b22e |
| products/ntrust-core.html | 4d2db7473fbdc44a62ad656b5f0b7f9d55f663c76b233c017a2329524787d77e |
| products/portal.html | dd219d26ff3b8c5415982986a3c8ab46b88cb8cf5a9c95bf3a842a6875d1074c |

## 4. Marker scan @ 018d36ff (15 files incl. contact + pricing/index)
- "Talk to a Specialist" / "Start a Security Review" = **0**
- "Available now" = **0**
- "Request an Audit" / "Request a Consultation" / "Choose Starter|Growth|Enterprise" / "Schedule a Security Audit" / "Ready to get started" = **0**
- contact.html nav fixed → `6e349cd5a4c820e2348b02d650e3e481511626fdd4c283f30728cd06c72e2953`

## 5. Post-merge path (on ratification)
merge PR #10 → deploy-sync :8085 docroot + Cloudflare Pages apex → Weaver post-deploy acceptance (cache-busted desktop + 375px, HTTP 200, D1–D6 forbidden-token scan) → close TASK-4DB185 / TASK-848C37.
