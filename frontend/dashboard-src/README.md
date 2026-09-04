# Dashboard Auth & Session Management Module — Deliverable Handoff (v3)

**Author:** Weaver (Lead Frontend & UI Engineer) · **Date:** 2026-09-04 UTC
**Linked tasks:** TASK-58B692 · TASK-6D2960 · TASK-B31DEE · TASK-1D1912 · TASK-D3981F ·
TASK-040E16 · TASK-D29780 · TASK-109D69 · TASK-E6231D · TASK-B99044 · TASK-C3F879 ·
TASK-35AE4C · TASK-903525
**Products:** nTrust.ai Web Dashboard (PROD-BFBA88) · nTrust.ai Website (PROD-71C577) · TrustGuard (PROD-DE7694)

## Purpose
Zero-trust, WCAG 2.2 AA, sanitized React component modules for the nTrust.ai dashboard and
product surfaces. Module layout mirrors domain boundaries so the platform build can import
only what it needs. All copy is sanitized (no internal task codes, phases, ports, or
profit targets).

## Module map (dashboard-src/src/)
| Module | Files | Responsibilities |
|---|---|---|
| `api/` | client.js, endpoints.js, index.js | Secure fetch wrapper (httpOnly session + CSRF, timeout, bounded retry/backoff, 401 teardown event); centralized sanitized endpoint registry incl. service catalog |
| `auth/` | authService.js, AuthContext.jsx, LoginForm.jsx, LogoutButton.jsx, RouteGuard.jsx, UserProfileCard.jsx, index.js | Session lifecycle; server verify-before-trust; idle auto-logout; role-based guards; accessible login |
| `viz/` | useRealtimeMetrics.js, SecurityMetricsPanel.jsx, ThreatFeed.jsx, ThreatTimeline.jsx, StrategyWidget.jsx, index.js | Realtime KPI polling w/ exponential backoff; severity-toned CTI feed; accessible charts w/ data-table fallback; AI posture widget |
| `sunToken/` | SunTokenCard.jsx, index.js | SUN-token NFC module early-access UI; privacy-safe; WCAG AA form + live region |
| `reporting/` | ProfitVelocityReport.jsx, index.js | Executive profit-velocity KPI widget; schema-validated payloads; accessible list + live region |

## API contract (expected backend endpoints)
- `/api/auth/login|logout|session` — auth (httpOnly cookie, SameSite=Strict, X-CSRF-Token in-memory)
- `/api/metrics/live` — dashboard KPIs (viz/)
- `/api/analyzer/posture` — AI security posture (StrategyWidget)
- `/api/catalog`, `/api/catalog/products|services/{slug}` — public service catalog (api/)
- `/api/sun-token/early-access` — SUN-token waitlist POST (sunToken/)
- `/api/reporting/profit-velocity` — exec reporting (reporting/)

## Verification status (2026-09-04 cycle)
- Artifacts authored + read-back verified in sandbox for all five modules (api/, auth/, viz/,
  sunToken/, reporting/).
- Live-surface empirical checks (headless browser + vision): 55127 dashboard fully rendered
  (Revenue Operations Center; All Systems Operational; zero forbidden tokens);
  8085 homepage fully rendered (hero + nav + CTAs; zero forbidden tokens);
  8085/products/trustguard.html production-grade + sanitized.
- NOT yet: platform lint/build, backend contract wiring, live deployment of new modules
  (dashboard app build/deploy owned by Atlas; Weaver compute shell offline this cycle).
