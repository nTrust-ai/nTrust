# 8085 Blank-Render Remediation — Evidence (2026-09-04 04:30 UTC)

**Author:** Atlas (Infrastructure & DevOps Director)
**Status:** OPEN — awaiting docker_restart authorization

## Finding (empirical)
- Screenshot `screenshots/33b850b0.png` (host vantage, 04:29 UTC): 8085 renders SOLID BLACK — zero elements.
- Container env_7624807f (port 8085) is running but serving the **React SPA shell** (docroot `/app/data/prod/www/index.html` — `<div id="root"></div>` + `/assets/index-B0K7Hm-f.js`), which fails at JS runtime → blank page (defect class RAID-B50692/596D17/AA2A68).
- Canonical static payload verified ON DISK at `/app/data/frontend/dist/index.html` (12,770 bytes, Sep 4 03:50, zero `<script>` tags, 0 forbidden tokens, 0 mailto). Pre-prune host-vantage matrix: 18/18 routes HTTP 200.

## Remediation command (requested)
Restart env_7624807f serving:
```
python3 -m http.server 8085 --directory /app/data/frontend/dist --bind 0.0.0.0
```
- Serves canonical multi-page static site (/, /contact.html, /spine.html, /404.html, /products/*.html x10, robots, sitemap).
- Contact POST `/api/contact` temporarily degraded (ntrust_web_server.py was container-local to pruned env_ee237d41; Developer to re-supply).

## Screenshots (evidence)
- Blank 8085: screenshots/33b850b0.png, screenshots/dca43241.png
- 9090 catalog PASS: screenshots/a4c450dc.png
- 7790 shield PASS: screenshots/6654a6ff.png
- 55127 dashboard PASS: screenshots/8e339045.png

## RAID
RAID-28903A (P0 regression — accidental prune + 8085 blank). Escalated to Nedo 04:35 UTC.
