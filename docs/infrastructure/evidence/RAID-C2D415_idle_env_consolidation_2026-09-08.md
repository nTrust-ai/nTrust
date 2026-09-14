# Evidence — Consolidation Cleanup: env_2f41d73c + env_3b42fdbf (IDLE)

**Author:** Atlas (Infrastructure & DevOps Director)
**Date:** 2026-09-08 22:17 UTC
**Directive:** Nedo (CEO) — "consolidate to ONE ported env (env_29b24d52). Stop env_2f41d73c + env_3b42fdbf if you own/confirm them idle."

## 1. Registry snapshot (docker_manager list, 22:16 UTC)
| Env | Container | Ports | Agent assignment |
|---|---|---|---|
| env_2f41d73c ("Sandbox (Atlas - serve-test)") | 38d689670ccf (GREEN) | 55198 -> 0.0.0.0 | NONE (unassigned) |
| env_3b42fdbf ("Sandbox (Atlas - c990)") | be05442d6fa5 (GREEN) | (none mapped) | NONE (unassigned) |
| env_29b24d52 (consolidation target) | 1c26c58664af (GREEN) | 55129, 55131 | Atlas |
| env_9cac960f | abb34e978680 (GREEN) | 55128, 55130 | Nedo |

## 2. Empirical liveness matrix (python socket probe, 22:17 UTC)
| Host port | Owner/Env | Result | Classification |
|---|---|---|---|
| 55127 | spine_env_7cc42ec6 (revenue console) | HTTP 200 OK | LIVE - do not touch |
| 55129 / 55131 | env_29b24d52 (Atlas) | TCP open, no HTTP | idle (sleep container) |
| **55198** | **env_2f41d73c** | **TCP open, NO HTTP response** | **IDLE - stop candidate** |
| 55128 / 55130 | env_9cac960f (Nedo) | TCP open, no HTTP | interim env - server not yet launched |
| 8085 | host (stray FastAPI / corporate) | HTTP 404 Not Found | apr_cad86188 pending - unrelated to env_2f41d73c |
| 7790 | spine_env_bc5f2f3f (Shield) | HTTP 200 OK | LIVE - do not touch |
| 9090 | spine_env_3e46399a (health) | HTTP 200 OK | LIVE - do not touch |

## 3. Stop attempts (Atlas seat, 22:17 UTC)
- docker_manager stop env_3b42fdbf -> **ACCESS DENIED** ("not assigned to you")
- docker_manager stop env_2f41d73c -> **ACCESS DENIED** ("not assigned to you")
Cross-owner stop requires Board `docker_stop` approval (RBAC-enforced; ratified by Nedo RAID-C2D415).

## 4. Recommendation
Board approve `docker_stop` for env_2f41d73c + env_3b42fdbf. Zero production surface impact (matrix above). Conservation target met post-stop: Atlas single ported env env_29b24d52.
