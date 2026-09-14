# CEO Routing Record — Atlas Execution Ask (5 Items + Port 8085 Collision)

**Date:** 2026-09-08
**Author:** Nedo (CEO · Board Delegate)
**Lane:** exec / website-launch
**Trigger:** Atlas execution ask (~09:05 UTC) + NEW port-8085 finding

## Summary
Atlas reports exec-lane work staged and pre-verified (PAT approvals apr_c1a21dae + apr_45055ed7 landed; main d46ef4db CI-green; 55127/7790/9090 reachable). Five (5) items require Naveed one-click to release under EU AI Act Art.14 (Human-in-the-Loop). Atlas also surfaces a NEW collision on host port 8085 that the Board must disposition.

## Items requiring owner gavel (Art.14)
1. **apr_66047cc3** → merge PR #12 (pricing fix, CI green).
2. **apr_794b192f** → merge PR #11 + PR #8 (asset sync + FRTS §5 evidence, CI green).
3. **apr_003ed2c7** → delete 4 orphan CI branches (TASK-4D3E26).
4. **apr_code_7ff8e778** → `_headers` cache-fix promotion.
5. **apr_ecdbb97d** → CF deploy-sync (capability-blocked: no CF creds in env_b774ca13).

## NEW FINDING — Port 8085 collision (for Board disposition)
- Host port **8085** is owned by critical core container **`spine-api-1`**.
- TASK-B78E52 (sidecar 8085 publish) cannot execute without displacing core.
- **Recommendation:** Architect/core verify whether `spine-api-1` already serves the React dist; if not, assign an alternate port for the SPA sidecar.
- RAID logged by Atlas.

## Governance posture
- $0 recognized · no self-approval · Art.14 HITL respected · no mutation without owner gavel.
- No fleet broadcast sent (stand-down honored).

## Request
Naveed one-click on `apr_66047cc3`, `apr_794b192f`, `apr_003ed2c7`, `apr_code_7ff8e778`, `apr_ecdbb97d`; plus disposition on the 8085 finding (verify spine-api-1 or assign alternate port).
