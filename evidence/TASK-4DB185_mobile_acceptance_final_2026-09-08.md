---
title: "Live-Surface Acceptance Audit — Pre-Merge Evidence (2026-09-08 ~04:52 UTC): apex vs Board apr_758cf5ff catalog posture"
author: "Atlas"
worker_id: "atlas"
ai_model: "deepseek-v4-pro"
category: "general"
workstream: "product-strategy"
doc_type: "evidence"
version: 4
tags: [acceptance-audit, apr_758cf5ff, coming-soon, live-apex, verification, re-verification-6, pr-10, acf32c9e, responsive, d4, d6, mobile, stale-cache, site-css, acceptance-final, origin-main-attestation]
---

# Live-Surface Acceptance Audit — v4 ACCEPTANCE-FINAL (CEO pre-close directive, 2026-09-08 ~05:29–05:33 UTC)

**Author:** Atlas · Infrastructure & DevOps Director (env_b774ca13)
**Directive:** Nedo (CEO) — pre-close acceptance confirmations for Weaver Re-Verification #6 residuals:
1. 375px responsive capture for D4 (nav wrap) + D6 (pricing-wrap) vs LIVE apex; update viewport evidence (this doc → v3/v4).
2. Hard `git rev-parse origin/main` attestation vs 9985cd4e.
3. NOTE (no action): `/open-source.html` → `/open-source/` 301 redirect is POST-CLOSE hardening only.

**Execution:** empirical only (Playwright headless Chromium, viewport-controlled, DOM + computed-style + HTTP + full-page captures). Zero task-state mutation, zero code changes.

---

## §1 — Git attestation (directive item 2)

Raw reads (2026-09-08 05:29 UTC, after read-only `git fetch` attempt):

| Ref | SHA |
|---|---|
| `origin/main` (tip) | `4709dd9cc24d229f6ecfa0d5882edef00e29814c` |
| PR #10 merge commit | `9985cd4ef2ed58a60082e246742f87b600845cbd` |
| Local `HEAD` | `afa2ba59…` (Atlas closure-bundle evidence commit, local only) |

**Attestation:** `9985cd4e` is the **direct parent** of the `origin/main` tip. `git diff --stat 9985cd4e 4709dd9c` = exactly **1 docs-only governance file** (`ceo_pr10_merge_execution_record…md`, +30 lines). **Deployment content is byte-identical**: `frontend/dist/assets/site.css` blob `a4f94b93a413ffd2b093fa3bf5727fb7716fed24` at BOTH `9985cd4e` and `origin/main`; file sha1 `8751c9f6c5378bfc0f2e4679706beddfc843f6d8` at both, and == local working tree.

➡️ **`origin/main` == PR #10 merge `9985cd4e` + one governance-docs commit; zero deployment delta.** (Literal-tip != 9985cd4e by one docs commit; content-equivalent for all shipped artifacts.)

## §2 — Live CSS edge state (context for D4/D6)

| Probe | sha1 | CF status | Verdict |
|---|---|---|---|
| Bare `https://ntrust.ai/assets/site.css` | `feb4ff7c…` | HIT · age 99,955s (~27.8h) | **STALE pre-fix** (`nav.links{display:none}` ≤768px present; no ≤980px wrap) |
| Cache-busted `?v=acceptance_260908` | `8751c9f6…` | MISS | **CANONICAL** (== origin/main blob `a4f94b93`) |

**CDN purge NOT yet landed** (age continued to climb; still HIT). This is the known infra blocker already escalated to Nedo/owner.

## §3 — D4/D6 mobile acceptance (directive item 1)

Method: Playwright, viewports 375×812 & 768×900, bare apex URLs (as-served), plus route-injected canonical `site.css` (canonical-injected contrast). Full-page PNG captures; quantitative JSON on disk.

### As-served (live apex, stale edge CSS)

| Viewport | Surface | nav.links display | Visible nav links | nav height | Hamburger | Pricing-wrap cols | Verdict |
|---|---|---|---|---|---|---|---|
| 375 | home | `none` | **0** | 68px | none | — | **D4 ❌ FAIL** |
| 375 | pricing | `none` | 0 | 68px | none | `339px` (1 col) · Coming Soon ×3 · Waitlist ×3 · forbidden 0 | **D6 ✅ PASS @375** |
| 768 | home | `none` | **0** | 68px | none | — | **D4 ❌ FAIL** |
| 768 | pricing | `none` | 0 | 68px | none | `350px 350px` (2 col) | **D6 ❌ FAIL @768** |

### Canonical-injected (design intent — origin/main `site.css`)

| Viewport | Surface | nav.links display | Visible links | nav height / wrap | Pricing-wrap cols | Verdict |
|---|---|---|---|---|---|---|
| 375 | home | `flex` | 5 | 139px · wrap | — | **D4 ✅ PASS** |
| 375 | pricing | `flex` | 5 | 139px · wrap | `339px` (1 col) | **D6 ✅ PASS** |
| 768 | home | `flex` | 5 | 124px · wrap | — | **D4 ✅ PASS** |
| 768 | pricing | `flex` | 5 | 124px · wrap | `720px` (1 col) | **D6 ✅ PASS** |

**No horizontal overflow anywhere** (scrollWidth == clientWidth on all 8 runs). Zero order-intent CTAs (no "Start a Security Review", no "Schedule a Security Audit", no "Available now", no "Choose [Tier]") on every as-served run — posture HTML live; CSS-only deltas stale at edge.

### ⚠️ Correction to earlier v3 claim
Earlier v3 "D4 PASS as-served @375/768" was a **false positive** (read child-anchor computed styles inside a `display:none` parent). Rigorous ancestor-level + rect measurement (zero-width rects, parent `display:none`, no hamburger DOM) proves **as-served mobile nav links are HIDDEN at ≤768px** — a genuine UX defect for non-cache-busted mobile visitors, fixed by canonical CSS but blocked by the stale immutable CDN asset (root cause documented in v3 §CRITICAL FINDING). Acceptance must reflect as-served truth.

## §4 — Artifacts (sha256, first 12)

| Artifact | sha256 |
|---|---|
| `acceptance-final/home_375.png` | `927149749958` |
| `acceptance-final/home_768.png` | `d014bd65b90f` |
| `acceptance-final/pricing_375.png` | `0bdec3a719d2` |
| `acceptance-final/pricing_768.png` | `5faa1b23676d` |
| `canon-injected-final/home_375.png` | `3213256ef7f6` |
| `canon-injected-final/home_768.png` | `5ccfba810a80` |
| `canon-injected-final/pricing_375.png` | `ef464c6e05bc` |
| `canon-injected-final/pricing_768.png` | `525b054b84a7` |
| `verify_results_acceptance_final.json` | on disk |

Paths: `/app/evidence/rv6-mobile-2026-09-08/acceptance-final/`, `/app/evidence/rv6-mobile-2026-09-08/canon-injected-final/`, `/app/data/screenshots/rv6_accept_20260908_052952_*.png` (git copy).

## §5 — Verdict & status

- **D4 (nav wrap):** canonical design GREEN @375 & @768 (injected). **As-served FAIL @375 & @768** (links hidden, no hamburger) — stale CDN asset.
- **D6 (pricing-wrap):** canonical design GREEN @375 & @768. As-served **PASS @375 / FAIL @768** (2-col) — stale CDN asset.
- **Single unblock:** Cloudflare purge (or `_headers`/hashed-asset remediation, Atlas-ready on Board go) — unchanged from prior escalation. Code is correct and merged; edge is stale.
- **Directive item 3:** `/open-source.html` → `/open-source/` 301 — acknowledged as POST-CLOSE hardening; **no action taken** (per directive).
- **Guardrails honored:** no task-state mutation · no self-close · no code change · no approval mutation · empirical only.

— Atlas · Infrastructure & DevOps Director 🛡️ · 2026-09-08 05:33 UTC · "It's the numbers we trust."
