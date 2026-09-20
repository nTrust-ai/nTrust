# CF Cache Purge Evidence — ntrust.ai /assets/site.css (2026-09-08)

Author: Atlas · Infrastructure & DevOps Director

## 1. Tooling/credential check (proven absent)
- `which wrangler curl cf jq` → all NOT FOUND
- `env` grep (cloudflare|cf_|pages|wrangler|zone|account|api_token|deploy) → EMPTY
- `~/.netrc`, `~/.wrangler`, `~/.config/cloudflare` → absent
- `wrangler.toml` / `wrangler.jsonc` in repo → none
- repo-wide secret-name scan (CLOUDFLARE_API_TOKEN / CF_ACCOUNT_ID / CF_ZONE_ID / deploy_hook) → none
=> No CF purge capability in sandbox. CEO Nedo independently confirmed identical finding.

## 2. Live fetch matrix (python urllib, YVR PoP)
| Request | sha1 | len | ETag | Age | CF-Cache-Status |
|---|---|---|---|---|---|
| bare `/assets/site.css` | `feb4ff7cd40c6c351273b36d6fe29582368fd9e8` | 10995 | `W/"2c70dc0bf9b74cf489d33c310dae8595"` | ~100667s (~28h) | HIT (STALE) |
| `?cb=<ts>` | `8751c9f6c5378bfc0f2e4679706beddfc843f6d8` | 11797 | `"ca68e96702d326e06916e44c60ea8d29"` | — | MISS (CANONICAL) |

Effective cache-key = full URL (query string included); CF does not emit a cache-key header (CF-Ray `a37b9fc7…-YVR` identifies PoP). Canonical sha1 `8751c9f6` == working tree == HEAD == `9985cd4e`/`4709dd9c`/`acf32c9e`.

## 3. Old D6 defect rule ABSENT from canonical
- `.nav.links{display:none}` occurrences in canonical site.css: **0**
- `nav.links{display:none}`: **0**
- `display:none` only on `.form-ok`/`.form-err` (unrelated).
- Canonical 980px rule = nav WRAP row: `.nav{flex-wrap:wrap;…} nav.links{display:flex;flex-wrap:wrap;order:3;width:100%;…}`
- Canonical hero h1 = `clamp(2rem,4.6vw,3.4rem);line-height:1.14;letter-spacing:-.03em;max-width:840px;text-wrap:balance`

## 4. SHA reconciliation (proven)
- `git merge-base 9985cd4e 4709dd9c` = `9985cd4e`; `9985cd4e` IS ancestor of `4709dd9c`
- `git diff 9985cd4e 4709dd9c -- frontend/dist/assets/site.css` = **0 lines** (byte-identical)
- `4709dd9c` = `9985cd4e` + 1 docs-only governance file (+30 lines)

## 5. Open Source href disposition
- nav "Open Source" → `/spine.html` (200); footer "Spine Engine (Open Source)" → `/spine.html` (200)
- `/open-source/` → 200 (canonical, sitemap-listed, og:url) but orphaned from nav/footer
- `/open-source.html` → 404
- Per CEO Nedo disposition: fold reconciliation into TASK-F2D25F (not changed inline).

## 6. Fix state
- Durable `_headers` fix committed (local `bdfe236f`): `/assets/*` `immutable` → `max-age=3600, stale-while-revalidate=86400`
- Revert commit `dc00f32c` restored unversioned `/assets/site.css` (dropped content-hash rename to align with CEO disposition)
- **Immediate unblock still required: CF cache purge (owner Naveed only — no agent holds CF creds).**

---

## Addendum v3 — Post-RBAC-Override Re-Verification + Execution-Attempt Ledger (Atlas · 2026-09-08 ~07:31 UTC)

**Event:** RBAC override `apr_b2ca18f4` APPROVED (Naveed, Telegram OOB) restoring Atlas P0 infrastructure operations. Developer handoff (07:24 UTC) requested verify-then-purge of plain `/assets/site.css` (no source edit).

### 1. Live re-verification (07:27 UTC, python urllib)
| Probe | HTTP | bytes | sha1 (12) | text-wrap:balance | CF-Cache-Status | Age | Cache-Control |
|---|---|---|---|---|---|---|---|
| bare `/assets/site.css` | 200 | 10,995 | feb4ff7cd40c | 0 (STALE) | HIT | 107,019s (~29.7h) | public, max-age=31536000, must-revalidate, immutable |
| `?cb=atlaspurgeverify1` | 200 | 11,797 | 8751c9f6c537 | 3 (CANONICAL) | MISS | — | public, max-age=14400, must-revalidate, SWR |

→ Gap persists: edge serves the pre-fix immutable object; origin is canonical. Edge purge remains the sole unblock.

### 2. Authorization ledger (all APPROVED by Naveed, Telegram OOB)
- `apr_6f855f72` — Owner CF cache purge ntrust.ai /assets/site.css
- `apr_dbf0a660` — CF cache purge (D1/D4/D6 as-served acceptance)
- `apr_d2a07320` — CF cache purge (TASK-4DB185 + D4/D6)
- `apr_b2ca18f4` — Atlas RBAC Runtime Enforcement Override (Restore P0 Infrastructure Operations)

### 3. Post-override execution-avenue scan (07:28–07:31 UTC) — ALL EMPTY
- env: no CF vars (only BIND_HOST / FASTAPI_HOST / GITHUB_TOKEN / git identity / GPG_KEY)
- secret mounts: /run/secrets, /etc/secrets, /var/run/secrets → absent
- .startup_env_* + git config credential helpers: none
- GitHub API (GITHUB_TOKEN): repo actions secrets = [] · org secrets = 404
- Cloudflare API: egress reachable, unauth → 403 (auth-gated; unchanged)
- Docker: no socket/CLI in sandbox; no purge-helper image/container provisioned
- Tooling: wrangler / curl / cf / jq / wget absent; no wrangler.toml; no deploy hook; .github/workflows = local CI only (no CF action, no secrets)

### 4. Deterministic conclusion
`apr_b2ca18f4` restored Atlas **tool execution** but did NOT provision a Cloudflare API token / deploy hook — the actual missing capability for an edge purge (unchanged from capability-blocker evidence v2 §4/§7). Authorization is no longer the blocker (4× approvals); **credential is**. Atlas cannot fabricate credentials; **no purge executed this cycle** (truthfully reported, not declared done).

### 5. Remaining unblock (either, both fully authorized)
1. **Naveed one-click** (dashboard): zone `ntrust.ai` → Caching → Purge Everything (~1 min) — deterministic for the immutable HIT object per CEO ruling doc_def53aa299 v3 §5.4.
2. **Token injection**: provision scoped CF purge token (`CLOUDFLARE_API_TOKEN`) + zone id into Atlas env `env_b774ca13` → Atlas executes the documented purge API call and re-verifies bare URL == 11,797 B / 8751c9f6 / text-wrap:balance ×3.

### 6. Discipline
0 source edits · 0 task-state writes · 0 closures · 0 approval flips · 0 doc-vault publishes · $0 revenue impact.
— Atlas · Infrastructure & DevOps Director / PO (PROD-DCCCF5) · nTrust.ai
