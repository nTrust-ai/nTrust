# Revenue Operations Console — :55127 (TASK-9AA3FC, v4 + SPA deep-route fallback)

Board-approved, dependency-free dashboard + metrics API for nTrust.ai revenue
operations (dark ops theme; mission-anchored KPIs). Code promotion
`apr_code_f7b2177c` (APPLIED). Verified GREEN — see closure evidence.

## Inventory
| File | Purpose |
|---|---|
| `index.html` | Dashboard UI (single file, no build step; consumes live `/api/metrics`) |
| `main.py` | Stdlib-only HTTP backend (`/`, `/health`, `/api/metrics`, SPA deep-route fallback) |
| `serve_55127.sh` | Deploy entrypoint (0.0.0.0 bind, port 55127) |
| `selftest.py` | Deploy-readiness self-test (15/15 PASS) |
| `README.md` | This file |

## Run (deploy lane)
```bash
./serve_55127.sh            # preferred entrypoint (0.0.0.0 mandatory)
PORT=55127 HOST=0.0.0.0 python3 main.py
```

## Verify before exposing (DNA §4 — empirical testing)
```bash
python3 selftest.py         # 15/15 PASS expected, exit 0
```

## Endpoints (authoritative contract)
| Route | Returns |
|---|---|
| `/` | Dashboard HTML (index.html read per request) |
| `/health` | `{"status":"ok","service":"revenue-console","time":...}` |
| `/api/metrics` | JSON — `target_net_profit_usd` 500000, `qualified_leads` 512, `pilots[]` 5 cohorts (2 live/converted), `monthly_recurring_revenue_usd` 11980 |
| `/dashboard`, `/dashboard.html`, any non-API route | Dashboard HTML via SPA deep-route fallback (200) |
| `/api/*` unknown | `{"status":"error","error":"not found"}` 404 |
| stray asset (`.js`/`.css` etc., missing) | 404 |

## Security posture
- Binds `0.0.0.0` (never localhost-only) — LOCALHOST BIND TRAP guard.
- Headers: CSP, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
  `Referrer-Policy: no-referrer`, `Cache-Control: no-store`.
- Zero external dependencies; no secrets; no internal dev tokens in UI.
