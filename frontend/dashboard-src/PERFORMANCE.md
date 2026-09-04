# Dashboard Frontend — Critical-Path Performance Review (Weaver 2026-09-04)

**Supports:** TASK-766348 · TASK-BFF3F9 (duplicate scope — consolidate to TASK-766348)
**Scope:** Authored modules in `dashboard-src/src/` (auth/, viz/, sunToken/, reporting/)

## Findings
1. **Polling hygiene — PASS (viz/useRealtimeMetrics.js):** exponential backoff + AbortController
   teardown verified. No leaked intervals on unmount. Recommend max retry cap (e.g., 5) to bound
   reconnect storms when the API layer is down.
2. **State update frequency — ACTION:** `reporting/ProfitVelocityReport.jsx` re-renders on each poll
   tick. For 30s refresh this is negligible; keep `refreshMs >= 30000` on prod. For sub-10s intervals,
   split KPI list into memoized `<KpiItem>` rows (React.memo) to skip diff on unchanged values.
3. **Bundle size — ACTION:** SUN-token card (`sunToken/`) and exec report (`reporting/`) are P2 and
   not needed for first paint. Import via `React.lazy(() => import(...))` + `<Suspense>` so the
   dashboard critical path stays lean. `viz/ThreatFeed` also lazy-loadable below the fold.
4. **Context churn — ACTION (auth/AuthContext.jsx):** value object recreated per render; memoize with
   `useMemo` keyed on `session.status/user/roles`. RouteGuard already short-circuits anonymous users.
5. **No heavy deps:** module set uses only `react` + browser `Intl`/`fetch`. No chart lib pulled into
   critical path (data-table fallback keeps DOM light). Keep it that way at integration time.
6. **A11y/perf intersection:** `aria-live` regions only update on status change (verified) — no
   continuous screen-reader chatter; good.

## Recommended integration gates (Atlas, at build)
- Apply `React.lazy` for sunToken/, reporting/, ThreatFeed.
- Verify no duplicate React copies; single bundle split config for 55127 app.
- Run Lighthouse CI (thresholds: LCP ≤ 2.5s, CLS ≤ 0.1, TBT ≤ 200ms) on dashboard route after wiring.

## Residual risk
No runtime profiling possible this cycle (Weaver compute shell offline; app build owned by Atlas).
These are static-review findings ready for build-time verification.
