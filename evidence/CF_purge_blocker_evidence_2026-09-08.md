# Atlas — CF Cache Purge Capability-Blocker Evidence

**Date:** 2026-09-08 UTC
**Author:** Atlas · Infrastructure & DevOps Director
**Classification:** P0 customer-facing compliance gap (TASK-4DB185 / D1 hero widow)

## 1. Live fingerprint — requested outcome NOT yet met
| Surface | HTTP | bytes | sha1 (12) | text-wrap:balance | CF-Cache-Status | Age |
|---|---|---|---|---|---|---|
| bare `https://ntrust.ai/assets/site.css` | 200 | 10,995 | feb4ff7cd40c | 0 (ABSENT) | HIT | ~100,177s (~27.8h) |
| cache-busted `?cb=…` | 200 | 11,797 | 8751c9f6c537 | 3 (PRESENT) | MISS | — |

→ The bare live URL still serves the **stale** `feb4ff7c` (10,995 B, no `text-wrap:balance`).
The requested outcome (bare URL = 11,797 B + text-wrap:balance) is **UNMET**.

## 2. Git state (fix is committed and pushed)
- HEAD = `afa2ba59`; origin/main = `4709dd9c`
- `site.css` blob = `a4f94b93` = sha1 `8751c9f6` = **11,797 B** (identical at HEAD and origin/main)
- The fix commit `6ea8596e` (TASK-4DB185) is present in both.

## 3. Root cause
`frontend/dist/_headers` carries `/assets/* → Cache-Control: public, max-age=31536000, immutable`,
pinning the CF edge cache to the pre-fix asset at the non-hashed `/assets/site.css` URL.

## 4. Atlas missing capabilities (exact) — UNABLE to self-execute
- `wrangler` NOT FOUND; `curl` NOT FOUND; `cf` NOT FOUND; `jq` NOT FOUND
- No Cloudflare env vars (CF_API_TOKEN / CLOUDFLARE_API_TOKEN / deploy hook) — `env` grep empty
- No `wrangler.toml` / `wrangler.jsonc` in repo
- `git remote` = https://github.com/ntrustai/nTrust.git — raw `git fetch`/`git push` has no credential (fatal: could not read Username)

## 5. Conclusion
The CF Pages **origin is already correct** (cache-busted = 8751c9f6 = 11,797 B), but the **edge cache
purge is the sole remaining unblock** and is an owner-level action Atlas cannot perform.

## 6. Requested next-owner action (concrete)
1. **Nedo**: perform the Cloudflare cache purge for `ntrust.ai` (`/assets/site.css` or zone-wide), OR
2. **Nedo/Naveed**: grant Atlas a purge capability (CF API token / `wrangler` / deploy hook), OR
3. **Naveed**: perform the owner one-click purge in the Cloudflare dashboard.
Durable prevention (drop `immutable`) = Weaver `apr_code_5b59d6a9` (PENDING Board), not promoted by Atlas.
