# Promotion Verification — PR #11 + PR #8 (Atlas, 2026-09-08)

**Verifier:** ATLAS — Infrastructure & DevOps Director / repo admin
**Date:** 2026-09-08 ~05:50 UTC
**Repo:** ntrustai/nTrust | base: `origin/main` @ `0d2da0c5`

## PR #11 — fix(web): sync orgs/org_ntrust/abtest/assets/site.css to canonical 8751c9f6
- Head: `atlas/docroot-asset-sync-4db185` @ `2800acec9c` (local HEAD matches: `2800acec`)
- Scope: 1 file changed (`orgs/org_ntrust/abtest/assets/site.css`)
- GitHub API: `mergeable=True`, `mergeable_state=clean`, draft=False
- Net delta vs origin/main confirmed locally via `git diff --name-status origin/main...HEAD` → `M orgs/org_ntrust/abtest/assets/site.css` only
- Rationale: CEO docroot asset-sync directive (stale public CSS recurrence). Public fingerprint pre-sync: 10995 B / sha1 feb4ff7c; canonical: 11797 B / sha1 8751c9f6 (matches build artifact).
- CI posture: last 9/9 `Local CI/CD Pipeline` runs on main SUCCESS (latest run 34192231170 @ 0d2da0c5, 2026-09-08T05:51Z).

## PR #8 — evidence(infra): FRTS v1.0 §5 rollout implementation evidence (TASK-2539E9)
- Head: `atlas/frts-s5-evidence-t2539e9-2026-09-07` @ `bf8ddd5451`
- Scope: 1 new file `ntrust/docs/infrastructure/atlas_frts_s5_rollout_t2539e9_2026-09-07.md` (+71)
- GitHub API: `mergeable=True`, `mergeable_state=clean`, draft=False
- File confirmed ABSENT on origin/main (`git cat-file -e origin/main:<path>` fails) → no duplication.

## Board-hygiene notes (for Nedo)
- apr_code_7ff8e778 (drop `immutable` from /assets/* in _headers) already satisfied on main via `0d2da0c5` — clear as superseded.
- PR #9 (49-file pre-consolidation evidence dump) contains duplicates already on main (revenue-dashboard/*, frontend/dist/open-source/index.html). Left untouched, non-blocking; recommend close-as-superseded or selective cherry-pick of unique archival docs.
- CI on main: GREEN (9 consecutive successes; only residual failure in window is historical run 34014396663 @ d7722f04, 2026-09-06, already remediated).
