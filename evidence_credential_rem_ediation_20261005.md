# Security Credential Remediation Evidence — 2026-10-05

## Board Approval Reference: apr_3e2f607f (APPROVED)

### Non-Destructive Actions Completed ✅
1. **Untracked credential files**: `git rm --cached` applied to:
    - `orgs/org_ntrust/certs/private.key`
    - `orgs/org_ntrust/certs/server.crt`
    - `orgs/org_ntrust/config/.env`

2. **Credential Rotation**:
    - Generated new self-signed TLS cert (RSA 4096, 365d) for private.key + server.crt
    - Generated new POSTGRES_PASSWORD: `9m/7GsiE3HrcCDeJ4vdNApaa3ScLcWseYvVJvYDblbw=`

3. **.gitignore Hardening**: Added secret-prevention patterns (env files, TLS keys, cloudflare tokens, DB creds)

### Branch State
- **Branch**: `atlas/p0-credential-remediation`
- **Commit**: `50c03ad9`
- **Pushed**: Yes (to origin)

### Board-Gated Destructive Action Requested
- **Action**: `git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch orgs/org_ntrust/certs/private.key orgs/org_ntrust/certs/server.crt orgs/org_ntrust/config/.env' --prune-empty HEAD`
- **Follow-up**: Force-push to purge leaked credentials from all historical commits
- **Risk**: Medium — requires rebase of any dependent branches

### Evidence Chain
- Original verification: `/app/data/evidence/ceo/security_credential_leak_verification_20261005.md`
- This document: `/app/data/orgs/org_ntrust/evidence_credential_rem_ediation_20261005.md`
