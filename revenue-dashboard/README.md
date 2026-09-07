# Revenue Operations Center — :55127 (TASK-9AA3FC)

Dependency-free dashboard + metrics API for nTrust.ai revenue operations.
Serves a dark-theme ops dashboard with mission-anchored KPIs ($500K+ annual net
profit target, 500+ qualified leads) and a graceful `/api/metrics` loader.

## Inventory
| File | Purpose |
|---|---|
| `index.html` | Dashboard UI (single file, no build step) |
| `main.py` | Stdlib-only HTTP backend (serves `/`, `/api/metrics`, `/health`) |
| `serve_55127.sh` | Deploy entrypoint (0.0.0.0 bind, port 55127) |
| `selftest.py` | Deploy-readiness self-test (run BEFORE exposing) |
| `README.md` | This file |

## Run (deploy lane)
```bash
# Preferred entrypoint (0.0.0.0 mandatory — localhost bind drops external traffic)
./serve_55127.sh

# Equivalent direct run
PORT=55127 HOST=0.0.0.0 python3 main.py
```

## Verify before exposing (DNA §4 — empirical testing)
```bash
python3 selftest.py    # boots on 0.0.0.0:55227, asserts endpoints/headers/metrics/bind
# Expected: "N/N checks passed" + exit 0
```

## Endpoints
| Route | Returns |
|---|---|
| `/` or `/index.html` | Dashboard HTML |
| `/api/metrics` | JSON: status, qualified_leads (500), net_profit_target (500000), pipeline/arr (live once telemetry wired) |
| `/health` | JSON: `{"status": "ok"}` |

## Security posture
- Binds `0.0.0.0` (never `127.0.0.1`) — see DNA "LOCALHOST BIND TRAP".
- Headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
  `Referrer-Policy: no-referrer`, `Cache-Control: no-store`.
- Zero external dependencies; no secrets or internal tokens in any artifact.
