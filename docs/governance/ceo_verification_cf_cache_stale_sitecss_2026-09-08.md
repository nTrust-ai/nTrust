# CEO Verification — Cloudflare Cache Stale `site.css` (unblocks TASK-4DB185 / D1–D6)

**Date:** 2026-09-08 ~05:24 UTC
**Author:** Nedo · CEO
**Origin:** Atlas escalation (Infrastructure & DevOps) — CF cache purge required.

## 1. Empirical verification (performed this cycle from CEO sandbox)

Tooling note: `curl`/`wget` absent in CEO sandbox; used Python `urllib` (read-only fetch, no CF write access). `env` grep for Cloudflare creds and `which wrangler` both EMPTY → **CEO cannot self-execute a purge** (no CF token/tooling).

| Probe | HTTP | sha1 (first 12) | CF-Cache-Status | Age |
|---|---|---|---|---|
| `https://ntrust.ai/assets/site.css` (bare) | 200 | `feb4ff7cd40c` | HIT | ~99,835s (~27.7h) |
| `https://ntrust.ai/assets/site.css?cb=1` (cache-busted) | 200 | `8751c9f6c537` | MISS | — |

Feature presence:

| Feature | bare (stale edge) | cache-busted (origin) |
|---|---|---|
| `text-wrap:balance` | absent | present |
| `max-width:840px` | absent | present |
| `letter-spacing:-.03em` | present | present |
| `clamp(2rem,4.6vw,…)` | present | present |

## 2. Root cause (confirmed)

Origin serves the **canonical, fixed** `site.css` (sha1 `8751c9f6`) that already contains `.hero h1 { … text-wrap:balance; max-width:840px }`. The bare URL is pinned by `_headers` → `Cache-Control: public, max-age=31536000, immutable` on `/assets/*`, so the CF edge keeps serving the **pre-fix** asset (`feb4ff7c`) at the non-hashed `/assets/site.css` URL.

**Conclusion:** No code change is needed for D1. The hero H1 widow fix (`text-wrap:balance`) is already landed in origin. The sole blocker is the stale CDN edge copy.

## 3. Disposition

1. **Immediate (owner one-click):** purge CF cache for `ntrust.ai` — URL `/assets/site.css` (or zone-wide). This alone makes D1/D6 live-verify green and unblocks TASK-4DB185; the code portion of TASK-AF07D1 is already satisfied.
2. **Durable (code, needs Board approval + promotion):** drop `immutable` from `/assets/*` in `_headers`; use short `max-age` + `must-revalidate` (e.g. `Cache-Control: public, max-age=3600, must-revalidate`). Prevents recurrence on every future CSS change. Assigned to Weaver (frontend lead) to prepare.
3. **Secondary (non-blocking):** reconcile "Open Source" canonical — nav+footer `/spine.html` (200) vs orphaned `/open-source/` (200) vs `/open-source.html` (404). Fold into TASK-F2D25F.

— Nedo · CEO 🛡️

---

## 4. Addendum v1.1 (2026-09-08 ~05:33 UTC) — Atlas corrective amendment & closure-gate status

Incorporated from Atlas doc_bfdfbff67a v4 (commit `331ee9f2`, git-vault synced), per radical-transparency discipline:

1. **Doc versioning:** Atlas's acceptance evidence chain is at **v4** (v3 content preserved verbatim; increment = corrective re-run + git attestation append). No evidence-version regression.
2. **Git attestation (exact-equality fails):** `origin/main` tip = `4709dd9c`, NOT `9985cd4e`. Relationship: `9985cd4e` is the DIRECT PARENT; delta = exactly 1 docs-only governance commit (`4709dd9c`, +30 lines, CEO PR #10 execution record); all deployment artifacts **byte-identical** (site.css blob `a4f94b93` at both; file sha1 `8751c9f6` == local tree).
3. **Acceptance status = BLOCKED / NOT CONFIRMED (as-served):**
   - **D4** as-served FAIL @375 & @768 — `nav.links` hidden (display:none), **no hamburger fallback** (earlier v3 "D4 PASS as-served" withdrawn as false positive: child-anchor styles read inside display:none parent).
   - **D6** as-served PASS @375 only / **FAIL @768** (pricing 2-col 350+350).
   - Canonical-injected runs GREEN (design correct) — but that is NOT what the live apex serves.
   - Root cause unchanged: **stale immutable CDN edge** — bare `/assets/site.css` = sha1 `feb4ff7c` (CF HIT, age ~99,955s ≈27.8h); cache-busted = canonical `8751c9f6`. **Purge has NOT landed.**

**Closure gate (recommended):** (a) Cloudflare purge lands → (b) bare `/assets/site.css` sha1 == canonical `8751c9f6` on re-verify → (c) D4/D6 PASS as-served @375 & @768. Alternative: Board may **explicitly accept the recorded as-served caveat** and close with it on record.


---

## 5. Addendum v1.2 (2026-09-08 ~05:37 UTC) — Final unblock path (deploy + purge)

Fresh live probe (CEO sandbox) after purge approvals landed:
- bare `/assets/site.css` → still 10,995 B, sha1 `feb4ff7c`, `Cache-Control: public, max-age=31536000, immutable`, age ~27.9h → **purge NOT yet landed at edge**
- cache-busted `?cb=ver2` → 11,797 B, sha1 `8751c9f6` → **origin FIXED**
- `site.8751c9f6.css` → 404 (content-hash rename reverted)
- live `_headers` `/assets/*` → still `immutable` (deploy NOT landed)

### Board state (verified this cycle)
| Request | Purpose | Status |
|---|---|---|
| `apr_6f855f72` / `apr_d2a07320` | CF cache purge (owner one-click) | APPROVED (Naveed OOB) |
| `apr_90b5d796` | Atlas closure-ready bundle (5 infra tasks @99%) | APPROVED (Naveed OOB) |
| `apr_code_5b59d6a9` | `_headers` TTL fix promotion (drop immutable) | PENDING Board |

### Durable fix — committed locally, NOT yet pushed to origin/main
- Local HEAD `dc00f32c`: `_headers` `/assets/*` → `max-age=3600, stale-while-revalidate=86400`; unversioned `site.css` retained (content-hash rename reverted to align with disposition).
- `origin/main` tip `4709dd9c` still carries `max-age=31536000, immutable`.

### Remaining unblock chain
1. Ratify `apr_code_5b59d6a9` → push main → CF Pages deploy `_headers` fix.
2. Execute CF purge one-click for `/assets/site.css` (approved; not yet landed).
3. Re-verify D1/D4/D6 **as-served** → close TASK-4DB185.

— Nedo · CEO 🛡️


---

## Addendum v1.3 — CEO Direct Re-verification Post-Approval (apr_6f855f72) · 2026-09-08 ~05:35 UTC

**Event:** Board approval `apr_6f855f72` (Owner CF cache purge `/assets/site.css`) marked APPROVED by Naveed ul via Telegram Out-of-Band.

**CEO direct verification (python3 urllib, browser UA, fresh cache-bust):**

| Probe | SHA1 (prefix) | CF-Cache-Status | Age | Cache-Control |
|---|---|---|---|---|
| PLAIN `/assets/site.css` | `feb4ff7cd40c` (STALE pre-fix) | HIT | ~100,500s (~27.9h) | `public, max-age=31536000, must-revalidate, immutable` |
| CACHE-BUST `?cb=<ts>` | `8751c9f6c537` (CANONICAL origin) | MISS | — | `public, max-age=31536000, must-revalidate, immutable` |

**Findings:**
1. The origin is **fixed** (canonical `8751c9f6` served on cache-bust).
2. The live **plain path is STILL RED**: sha1 `feb4ff7c`, CF HIT, Age ~27.9h. The approved purge has **not yet landed/propagated** on the edge.
3. Live `_headers` **still emits `immutable` + max-age=31536000** on BOTH paths → the durable `_headers` fix (drop `immutable`, short max-age + `must-revalidate`) is **NOT yet deployed** (TASK-AFF2AB lineage).

**Conclusion:** Approval ≠ purge-executed. Re-verify criteria for TASK-4DB185 remain **UNMET**:
- (a) dist deploy-sync incl. `_headers` — PENDING (gated by code-promotions `apr_code_5f51feb7` / `apr_code_b4534c2b`).
- (b) CF purge one-click — **authorized but not yet executed**; plain path still HIT on stale asset.

No gates flipped · no self-close/approve · TASK-4DB185 remains HOLD. — Nedo · CEO

---

## Addendum v1.4 — CEO Direct Re-Verification · 2026-09-08 ~09:07 UTC

**Event:** Post-approval re-probe (python3 urllib, browser UA). Purge authorized by apr_6f855f72 (~05:35 UTC) remains UNEXECUTED at edge.

| Probe | HTTP | sha1 (prefix) | CF-Cache-Status | Age | Cache-Control | text-wrap:balance |
|---|---|---|---|---|---|---|
| PLAIN /assets/site.css | 200 | feb4ff7cd40c (STALE pre-fix) | HIT | 113,014s (~31.4h) | public, max-age=31536000, must-revalidate, immutable | 0 |
| CACHE-BUST ?cb=ts | 200 | 8751c9f6c537 (CANONICAL) | MISS | — | public, max-age=14400, must-revalidate, stale-while-revalidate=86400 | 3 |

**Findings:**
1. Origin `_headers` durable fix HAS partially landed (cache-busted path now serves max-age=14400, was 31536000+immutable).
2. The live PLAIN path is STILL RED: sha1 feb4ff7c, CF HIT, Age ~31.4h — the Naveed-approved purge (apr_6f855f72) has NOT been executed/propagated on the edge.
3. TASK-4DB185 / TASK-AF07D1 D1–D6 re-verify criteria remain UNMET. Sole remaining blocker = edge purge execution (owner manual CF one-click or scoped CF API token for Atlas lane). Atlas capability-blocked (apr_ecdbb97d PENDING, assigned nedo @infrastructure).

No gates flipped · no self-close/approve · TASK-4DB185 remains HOLD. — Nedo · CEO
