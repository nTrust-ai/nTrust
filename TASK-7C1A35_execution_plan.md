# TASK-7C1A35 — GitHub PAT Provisioning + Cloudflare Pages Deploy: Execution & Rollback Plan

## Objective
Unblock CI/CD and Cloudflare Pages deployments for ntrust.ai (marketing) and
spine.ntrust.ai (portal) by provisioning a fresh least-privilege GitHub PAT and
completing the canonical push.

## Current verified state (2026-09-08)
- Target monorepo: `ntrustai/nTrust` (org also referenced as `nTrust-ai`).
- Blocker: GitHub API returns HTTP 401 "Bad credentials" — no valid PAT in the
  credential store (RAID-393B24 / RAID-9C3CDC / RAID-AC708E).
- Platform defect: `org_manager.configure_git` backend bug blocks in-band PAT
  rotation (RAID-735F6C / RAID-795340).
- Canonical board approval `apr_e9c2b3ea` is PENDING (RAID-F2D494).

## PAT provisioning steps (owner/Nedo lane)
1. GitHub → Settings → Developer settings → Personal access tokens →
   Fine-grained tokens → Generate new token.
2. Resource owner: `ntrustai` (reconcile with `nTrust-ai` org).
3. Repository access: Only select repositories → `ntrustai/nTrust`.
4. Permissions (least privilege):
   - Contents: Read and write
   - Workflows: Read and write
   - Pages: Read and write
   - Deployments: Read and write
5. Expiration: 90 days.
6. Rotate into credential store via `org_manager.configure_git` (after backend
   defect RAID-735F6C is patched) or inject as org secret `GH_PAT`.

## Deploy commands (executor/Atlas lane, post-PAT)
```bash
git -C /workspace remote set-url origin https://x-access-token:${GH_PAT}@github.com/ntrustai/nTrust.git
git -C /workspace fetch origin
git -C /workspace push origin main
```
Cloudflare Pages: confirm build output dir (`dist` vs `public`), confirm
`_redirects` www rule (RAID-1C2437), then trigger production build.

## Validation (non-negotiable empirical gates)
- `curl -s -o /dev/null -w "%{http_code}" https://api.github.com/orgs/ntrustai` → 200
- `curl -s -o /dev/null -w "%{http_code}" https://ntrust.ai/` → 200
- Cloudflare Pages production build → SUCCESS (no failed build)
- Forbidden-token scan of public output → zero PAT/secret strings

## Rollback plan
- Pages build failure → Cloudflare dashboard → Deployments → Rollback to last
  healthy production build.
- PAT exposure → GitHub → Settings → Developer settings → Revoke token;
  provision fresh PAT immediately.
- Keep prior build artifact tagged for instant re-deploy.

## Immediate request
Approve `apr_e9c2b3ea` (or this request) so the PAT can be provisioned, then
Atlas executes the push. DevArchitect requests explicit permission to proceed
with TASK-7C1A35 verification the moment the PAT is live.
