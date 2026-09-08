# Port 55127 Revenue Console — Restore Evidence (Atlas, 2026-09-08)

**Verifier:** ATLAS — Infrastructure & DevOps Director
**Sandbox:** env_b774ca13 (172.18.0.21)
**Date:** 2026-09-08 ~06:25 UTC

## Execution
Deployed Revenue Operations Console from `/app/data/revenue-dashboard` via `bash serve_55127.sh` (deploy entrypoint TASK-9AA3FC, binds `HOST=0.0.0.0 PORT=55127` — Localhost Bind Trap guard).

## Empirical verification matrix (python stdlib, no curl)
| Probe | Result |
|---|---|
| TCP connect 127.0.0.1:55127 | connect_ex=0 ✅ |
| GET / | 200 · text/html · 8797 B · title=Revenue Operations Console ✅ |
| GET /revenue/overview (SPA deep-route) | 200 · index.html fallback ✅ (TASK-D19901 acceptance) |
| GET /api/nonexistent | 404 · application/json ✅ |
| GET 172.18.0.21:55127/ (non-loopback) | 200 · 8797 B ✅ external-interface bind (0.0.0.0) |

## Visual proof
Screenshot: `/app/data/orgs/org_ntrust/screenshots/a13792c2.png` — vision-verified: fully functional dashboard, "console online" green indicator, KPI cards ($500K USD/yr target, 512 qualified leads, 5 pilot cohorts, $11,980 USD/mo MRR), PIL-001→005 pipeline table (Live/Pipeline/At Risk). NOT blank/error.

## Residual (external path)
Sandbox-internal exposure restored. Public internet reachability requires the host-level port publish / tunnel mapping for 172.18.0.21:55127 (outside sandbox scope; infra owner / Board). Old trycloudflare tunnels probed are DEAD (DNS NXDOMAIN). No agent holds CF credentials — purge/publish actions remain Naveed-only.
