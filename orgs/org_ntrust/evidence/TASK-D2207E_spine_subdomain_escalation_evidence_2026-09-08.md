# TASK-D2207E — spine.ntrust.ai Subdomain Convergence Blocker — Evidence (2026-09-08 04:05–04:20 UTC)

**Author:** Developer (agt_1eed2145) | **Env:** env_7cc42ec6 | **Doc ref:** doc_772412dbfb v3

## 1. Empirical probe summary (python3 stdlib + headless capture + vision)

| Surface | DNS | Server | Size / sha256 | Hero |
|---|---|---|---|---|
| spine.ntrust.ai | 216.198.79.65 (resolves; was NXDOMAIN 09-07) | Vercel | 26,592 B / 537792b3… | STALE LEGACY: H1 `Autonomous Agentic Infrastructure`, badge `Spine Hub is now live`, primary CTA `Get a License →`, ISO 27001 sub |
| ntrust.ai/spine.html | 172.67.211.81 | cloudflare | 7,802 B / abbc252c… | REFRAME LIVE: badge `Open Source · Bring Your Own AI`, H1 `Run autonomous AI organizations on your infrastructure`, CTAs `Get Started on GitHub →` + `View Documentation` |
| ntrust.ai/spine | 172.67.211.81 | cloudflare | 7,802 B / ff89795e… | REFRAME LIVE (same as /spine.html) |

Screenshots: screenshots/b7509cc1.png (stale subdomain), screenshots/b2048e3c.png (apex reframe).

## 2. Repo-source verification (github.com/ntrustai/nTrust, token-authenticated)

- Apex source = main `frontend/dist/spine.html` (7,209 B, reframe markers FOUND) → Cloudflare Pages ntrust.ai. REFRAME AT SOURCE ✅
- Standalone subdomain reframe source = branch `dev/spine-engine-landing` @27549b37, `landing-pages/spine.ntrust.ai/index.html` (31,331 B; H1 `Run autonomous AI organizations`, BYO badge, GitHub-first CTA) — committed, NOT merged to any Vercel-watched ref.
- Legacy page source: path `landing-pages/spine.ntrust.ai/index.html` has ZERO commits on main history; file 404s on main and master refs → the Vercel-served legacy build is NOT sourced from reachable ntrustai/nTrust branches.

## 3. Credential check

Sandbox env: GITHUB_TOKEN only. No VERCEL_*, CF_*, CLOUDFLARE_*, vercel.json, or wrangler config present. Developer cannot trigger Vercel redeploy or DNS change.

## 4. Conclusion / escalation

TASK-D2207E Developer scope COMPLETE; apex parity LIVE. Residual blocker = spine.ntrust.ai subdomain serves stale legacy (Vercel) — convergence requires external-owner action:
- Option A (recommended): nedo/Cloudflare-admin re-point spine.ntrust.ai CNAME → CF Pages host (TASK-8A5E75).
- Option B: Atlas Vercel redeploy from dev/spine-engine-landing@27549b37 (TASK-63AEAE/TASK-34E9AF).

Then owner gate apr_59071aad (Nedo/Tier-3) resolves TASK-D2207E 99→100. No live-surface mutation by Developer.
