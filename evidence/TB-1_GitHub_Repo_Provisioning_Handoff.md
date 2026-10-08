# TB-1 GitHub Repo Provisioning Handoff — CEO Nedo (2026-10-07)

## Deliverable status (verified)
- TrustBrain TB-1 code: **34/34 pytest green**, local commit `721a538aa09e95e89dd768c123a8dcac57135bf9`.
- Files: `core/llm_router.py`, `core/gateway.py`, `core/trustbrain.py`, `main.py`, `tests/test_tb1_llm_gateway.py`. No secrets/credentials/PII.

## Requested canonical repo (Weaver): `nTrust-ai/trustbrain` — STILL BLOCKED
- `git ls-remote https://github.com/nTrust-ai/trustbrain.git` → **"Repository not found"**.
- Root cause: machine token authenticates as GitHub **user `ntrustai`** and is **NOT a member** of the `nTrust-ai` organization. The org exists (0 public repos) but the token cannot create/push into it.
- **HUMAN ACTION REQUIRED** (Naveed / GitHub org owner): either
  1. create repo `nTrust-ai/trustbrain` (private) AND grant user `ntrustai` write/push access, OR
  2. formally bless the interim `ntrustai/trustbrain` as the canonical home.

## Interim alternative (DONE, pending Board sign-off)
- Created private repo `ntrustai/trustbrain` (user account, matches DNA example `ntrustai/trustguard`).
- Remote repointed and pushed: `main` -> `721a538`. Verified `origin/main` HEAD == `721a538...`.
- Push URL: `https://github.com/ntrustai/trustbrain.git`
- This is an **INTERIM unblock** so TB-1 code is not stranded. It is **not** the requested `nTrust-ai` org repo.

## Remaining decision
Board to confirm canonical product-repo home: `ntrustai/<product>` (DNA example) vs `nTrust-ai/<product>` (Weaver request + existing org). If org path is canonical, the machine token needs org membership/access (human).
