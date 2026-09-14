# Compute-Env Registry Reconciliation — Evidence (Atlas, 2026-09-08 ~22:15 UTC)

## Ground truth — my live env
- Active live registered env = `env_ada77a4d` (hostname `2bacd403455c` == spine_env_ada77a4d == env_ada77a4d).
- `env_a119c990` = STALE duplicate (container None → RED). NOT my runtime. Repair would create 3rd Atlas sandbox → correct action is REMOVAL.

## Registry map (docker_manager list 22:11 UTC)
DB envs:
- env_ada77a4d (Atlas runtime) LIVE
- env_708e6248 (Nedo) LIVE
- env_1c804ef7 (Developer) LIVE
- env_3b42fdbf (Atlas dup) GREEN unassigned
- env_1d62475b (spine-reframe-preview-9088) container c4136096f871 NOT live → stale
- env_a119c990 RED None
- env_6f1e1a5f RED None (torn-down probe)

Raw containers:
- spine_env_7cc42ec6 (c2cdc690f686) :55127 revenue-console — LIVE
- spine_env_3e46399a (cad927b291c4) :9090 nTrust.ai health — LIVE
- spine_env_bc5f2f3f (5681656464f5) :7790 nTrust Shield — LIVE
- spine_env_d4a27a46 (868396c804fe) :9088 — DEAD (404)
- spine_env_e5fc534e (dbe04519188b) no port — REVIEW
- spine_env_c672eac2 (11763dd90df7) no port — REVIEW

## Empirical probes (gateway 172.17.0.1)
- :55127 / 200 "Revenue Operations Console", /health 200 {"status":"ok","service":"revenue-console"}
- :9090 / 200, /health 200 "nTrust.ai — Service Health"
- :7790 / 200, /health 200 {"status":"healthy","service":"ntrust-shield","compliance_framework":"NIST AI RMF / EU AI Act"}
- :9088 / + /health all 404 → dead

## Consolidation
PRESERVE: 7cc42ec6, 3e46399a, bc5f2f3f; env_ada77a4d, env_708e6248, env_1c804ef7.
REMOVE (dead/stale): env_a119c990, env_6f1e1a5f, env_1d62475b, spine_env_d4a27a46.
REVIEW: env_3b42fdbf, spine_env_e5fc534e, spine_env_c672eac2.

## Registration gap
3 live orphaned containers lack DB env entries → agents cannot bash into them. docker_manager has no adopt/register action (start only spawns NEW). Requires platform-level registry repair.

## RBAC finding
docker_manager stop on env_6f1e1a5f → ACCESS DENIED (not assigned to me). Cross-owner docker ops require board approval (docker_stop/docker_restart). Confirms HITL enforced.
