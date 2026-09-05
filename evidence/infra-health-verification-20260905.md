# Infrastructure Health Verification Evidence — 2026-09-05 01:12 UTC
Prober: Atlas | Vantage: host.docker.internal (host)

| Port | HTTP | Content | Bytes | Sanitization |
|------|------|---------|-------|--------------|
| 55127 | 200 | nTrust.ai Revenue Operations Center | 13253 | clean |
| 9090 | 200 | Service Catalog v2.0 | 7597 | clean |
| 7790 | 200 | nTrust Shield | 2380 | clean |
| 7790/health | 200 | {"status":"healthy","service":"ntrust-shield","compliance_framework":"NIST AI RMF / EU AI Act"} | - | clean |
| 8085 | 200 | Autonomous Security & Compliance Solutions | 12786 | Coming Soon flags only |
| 55232 | 200 | board-test | - | clean |

Live containers: env_8394b3fd(9090), env_b1f0d335(restarted OK), env_685ee66a, env_9fbc7d05(55127/7790/55232), env_9c119be7, env_09cee96a(8085).
Action: docker_restart sweep pending board approval per apr_61c28181 owner directive.
