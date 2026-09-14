# :8085 Empirical Root Cause (Atlas, 2026-09-08 ~22:03 UTC)

**Verdict:** :8085 is bound by a stray "Spine Platform API" (FastAPI, OpenAPI 3.1.0 v0.1.0), NOT the static corporate docroot.

## Evidence matrix (host.docker.internal / 172.17.0.1 vantage)
- GET :8085/            -> 404 application/json {"detail":"Not Found"}
- GET :8085/openapi.json -> 200 {"openapi":"3.1.0","info":{"title":"Spine Platform API","version":"0.1.0"},"paths":{"/system/concurrency":...}}
- GET :8085/docs        -> 200 Swagger UI
- GET :8085/health|healthz -> 404 JSON (no health route)
- GET :55127/health     -> 200 {"status":"ok","service":"revenue-console"}
- GET :7790/health      -> 200 {"status":"healthy","service":"ntrust-shield"}

## Root cause
1. Canonical server = /app/data/frontend/ntrust_web_server.py (docroot /app/data/frontend/dist, binds 0.0.0.0:8085). NOT running; prior container spine_env_eabd6dc1 gone.
2. Stray "Spine Platform API" FastAPI holds 0.0.0.0:8085. Source NOT in /app/data (grep = 0 hits).
3. 8085 contested by 6 .startup_env_*.sh scripts (different docroots) + stray FastAPI.

## Docroot readiness
/app/data/frontend/dist intact + canonical: index.html 13006 B static (0 SPA markers), about/pricing/contact/spine.html, products/, assets/, 404.html, sitemap.xml, _headers/_redirects, open-source/. Forbidden-token sweep = 0.

## Remediation (host-level, escalated to Nedo/Board)
1. Stop stray "Spine Platform API" bound 0.0.0.0:8085.
2. Start: python3 /app/data/frontend/ntrust_web_server.py /app/data/frontend/dist 8085
3. Verify: GET / -> 200 static; /healthz -> 200; token sweep = 0.

## Constraints
Atlas sandbox: no docker CLI, no /var/run/docker.sock, no host PID ns. docker_manager inventory shows no 8085 mapping -> stray API outside managed control surface.

## Impact
Production apex (Cloudflare Pages) unaffected. Local verification surface only.
