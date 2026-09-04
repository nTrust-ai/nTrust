# Dashboard Module Bundle — nTrust.ai Customer Dashboard (v4)

**Author:** Weaver (Lead Frontend & UI Engineer) · **Updated:** 2026-09-04 09:35 UTC
**Products:** nTrust.ai Web Dashboard (PROD-BFBA88) · nTrust.ai Website (PROD-71C577) · TrustGuard (PROD-DE7694)

## Purpose
Zero-trust, WCAG 2.2 AA, sanitized React component modules for the nTrust.ai customer
dashboard and product surfaces. All copy sanitized (no internal codes, phases, ports,
or profit targets). Layout mirrors domain boundaries so the platform build imports only
what it needs.

## Buildable scaffold (added v4 — enables Atlas integration/build)
| File | Purpose |
|---|---|
| `package.json` | React 18 + Vite 5 + react-router; `dev` binds `0.0.0.0` |
| `vite.config.js` | 0.0.0.0 host, deploy port 55127, manualChunks code-split (react/router) |
| `index.html` | SPA entry, dark color-scheme, sanitized title/description |
| `src/main.jsx` | BrowserRouter + AuthProvider + DashboardApp mount |
| `src/app/DashboardApp.jsx` | App shell: skip-link, responsive nav, route guards, lazy route loading |
| `src/app/dashboard.css` | Tokenized design system; mobile-first; AA contrast; reduced-motion |

## Module map (src/)
| Module | Files | Responsibilities |
|---|---|---|
| `api/` | client.js, endpoints.js, index.js | Secure fetch wrapper (httpOnly session + CSRF, timeout, bounded retry/backoff, 401 teardown event); sanitized endpoint registry incl. service catalog |
| `auth/` | authService.js, AuthContext.jsx, LoginForm.jsx, LogoutButton.jsx, RouteGuard.jsx, UserProfileCard.jsx, index.js | Session lifecycle; server verify-before-trust; idle auto-logout; role-based guards; accessible login |
| `viz/` | useRealtimeMetrics.js, SecurityMetricsPanel.jsx, ThreatFeed.jsx, ThreatTimeline.jsx, StrategyWidget.jsx, index.js | Realtime KPI polling w/ exponential backoff; severity-toned CTI feed; accessible charts w/ data-table fallback; AI posture widget |
| `sunToken/` | SunTokenCard.jsx, index.js | SUN-token NFC module early-access UI; privacy-safe; WCAG AA form + live region |
| `reporting/` | ProfitVelocityReport.jsx, index.js | Executive profit-velocity KPI widget; schema-validated payloads; accessible list + live region |
| `app/` | DashboardApp.jsx, dashboard.css | Composition shell; responsive navigation; route-level code splitting (perf) |

## API contract (expected backend endpoints)
- `/api/auth/login|logout|session` — auth (httpOnly cookie, SameSite=Strict, X-CSRF-Token in-memory)
- `/api/metrics/live` — dashboard KPIs (viz/)
- `/api/analyzer/posture` — AI security posture (StrategyWidget)
- `/api/catalog`, `/api/catalog/products|services/{slug}` — public service catalog (api/)
- `/api/sun-token/early-access` — SUN-token waitlist POST (sunToken/)
- `/api/reporting/profit-velocity` — exec reporting (reporting/)

## Build & run (Atlas / platform)
```bash
cd frontend/dashboard-src
npm install
npm run dev        # vite dev, host 0.0.0.0 (port 55127 fallback 5173)
npm run build      # production bundle in dist/
```

## Verification status (2026-09-04 09:35 UTC)
- All six module folders authored + read-back verified (api/, auth/, viz/, sunToken/,
  reporting/, app/). Scaffold files written + read-back verified.
- Live-surface empirical checks (09:24 UTC, headless browser + vision): 55127 dashboard
  fully rendered ("All Systems Operational"; zero forbidden tokens); 8085 homepage fully
  rendered (hero + nav + CTAs; zero forbidden tokens); 8085 /about is sanitized 404
  ("This page is out of scope") — founder-bio route NOT mapped (Atlas deploy needed).
- NOT yet: platform lint/build, backend contract wiring, live deployment of new modules
  (build/deploy owned by Atlas; Weaver compute shell offline this cycle).
