# Branch Cleanup Decision — 4 Orphan Feature Branches (CI Failing, No Open PRs)

**Author:** ATLAS — Infrastructure & DevOps Director / repo admin
**Task:** TASK-D51D6E
**Date:** 2026-09-08 ~05:50 UTC
**Repo:** ntrustai/nTrust | base: `origin/main` @ `0d2da0c5` (2026-09-08 05:51Z)
**Classification:** Repo administration — decision record. No credentials/secrets.

---

## 1. Scope

The 4 orphan feature branches are all CI-failure remediation branches that (a) have no open PR,
and (b) are NOT merged into `origin/main`. They were cut to fix the historical `flake8` fatal-code
(E999/F821) gate that blocked CI on `main` tip `d7722f0` (2026-09-06, run 34014396663 — FAILED).

## 2. Branch Assessment (empirically verified via `git`)

| # | Branch | Unique commits vs origin/main | Last commit | Disposition |
|---|--------|-------------------------------|-------------|-------------|
| 1 | `feature/ci-flake8-fatal-fix` | 2 (`f37777f1`, `6b042490`) | 2026-09-06 | SUPERSEDED |
| 2 | `fix/ci-flake8-fatal-codes-TASK-24A6B8` | 1 (`6b042490`) | 2026-09-06 | SUPERSEDED |
| 3 | `fix/ci-fatal-flake8-main-d7722f0` (remote) | 0 | 2026-09-07 | SUPERSEDED |
| 4 | `fix/flake8-fatal-rot-weaver-20260906` (remote) | 0 | 2026-09-06 | SUPERSEDED |

## 3. Verification — fixes already landed on `origin/main`

`git log origin/main` confirms the CI remediation is already merged and green:

- `75aecfd0` Merge PR #3 — `fix(ci): clear fatal flake8 E999/F821 gate on main` (CI-green `fd4de280`)
- `cf4501ab` merge: land PR #2 (weaver flake8 rot fix) — 10 overlapping files resolved to PR #3 side
  (equivalent E999/F821 remediation, black-formatted, CI-green); pytest.ini pythonpath deduped.
- On-main CI commits: `fd4de280`, `dc6386cf`, `56ae465a`, `78f6ba9b`.

Main CI posture is GREEN (9 consecutive `Local CI/CD Pipeline` successes; residual failure is the
historical `d7722f0` run, already remediated). None of the 4 branches carry unique work not already on main.

## 4. Decision

DELETE all 4 branches (superseded — zero unique work at risk):

1. `feature/ci-flake8-fatal-fix` — DELETE (2 commits superseded by PR #3 equivalent remediation)
2. `fix/ci-flake8-fatal-codes-TASK-24A6B8` — DELETE (1 commit superseded)
3. `fix/ci-fatal-flake8-main-d7722f0` — DELETE (0 unique commits; fully on main)
4. `fix/flake8-fatal-rot-weaver-20260906` — DELETE (0 unique commits; fully on main)

No REVIVE required — no orphan branch contains work absent from `origin/main`.

## 5. Governance (EU AI Act / NIST AI RMF)

- Destructive repo mutation (remote `push --delete`) is a high-risk action → HITL.
  Atlas does NOT self-execute remote deletion. Board approval requested.
- This decision record is the audit-trail artifact (EU AI Act Art.12).
- Reversibility: branches remain recoverable via `git reflog` (local) and GitHub remote ref retention
  until deletion is executed.

— ATLAS · Infrastructure & DevOps Director · nTrust.ai
