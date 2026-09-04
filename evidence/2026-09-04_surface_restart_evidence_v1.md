# Surface Restart Evidence — Global Container Recovery (2026-09-04 ~06:45 UTC)

**Author:** Atlas (Infrastructure & DevOps Director)
**Trigger:** Board reviewer directive on apr_61c28181 — "restart all docker containers and resubmit request when they are all live again" (global container wipe ~06:30 UTC).

## Empirical verification matrix (host.docker.internal vantage, env_9fbc7d05, 2026-09-04 06:44–06:46 UTC)

| Surface | Port | Path | Result | Payload |
|---|---|---|---|---|
| RevenueOps Dashboard | 55127 | / | HTTP 200, 13,253 B | org_ntrust/dashboard/index.html (CEO baseline 13,253B ✓) |
| Service Catalog v2.0 | 9090 | / | **DEGRADED** — TCP accept, zero-byte response (RemoteDisconnected ×3) | prod/catalog/index.html (7,606B) — server wedged in env_b88c03b1 |
| nTrust Shield MVP | 7790 | / | HTTP 200, 2,281 B | shield_site landing page |
| nTrust Shield MVP | 7790 | /health | HTTP 200, 114 B | JSON NIST AI RMF / EU AI Act |
| Board manual-test | 55232 | / | HTTP 200, 85 B | JSON {"status":"healthy","service":"health-check"} |
| Corporate Site (SPA→static) | 8085 | / | HTTP 200, 12,770 B | frontend/dist/index.html — root now maps correctly (blank-root defect RESOLVED) |
| Corporate Site | 8085 | /healthz | HTTP 200, 165 B | ntrust-corporate-site JSON |
| Corporate Site | 8085 | /contact.html | HTTP 200, 8,242 B | Contact page |

## Hosting topology (post-recovery)
- env_9fbc7d05 (Atlas assigned): 55127 + 7790 + 55232 servers running (http.server / shield_server.py / health JSON).
- env_09cee96a (Developer-Remediation-Env): 8085 corporate ntrust_web_server.py serving frontend/dist — canonical, /healthz 200, root non-blank.
- env_b88c03b1 (orphaned, unassigned): 9090 catalog http.server WEDGED (accepts TCP, never responds). Needs docker_stop to release host 9090.

## Requested action
docker_stop env_b88c03b1 → spawn fresh 9090 catalog host → serve /app/data/prod/catalog → re-verify HTTP 200 → resubmit apr_61c28181.
