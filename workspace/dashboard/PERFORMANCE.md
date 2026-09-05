# nTrust.ai Dashboard — Performance Optimization Review

**Deliverable for**: TASK-BFF3F9 / TASK-766348 (Critical Path Code Review & Deployment Prep)
**Owner**: Weaver (Lead Frontend & UI Engineer)
**Target**: Core Web Vitals (LCP < 2.5s, INP < 200ms, CLS < 0.1), bundle < 200 KB gz initial

## 1. Critical-path findings

| # | Finding | Severity | Fix applied |
|---|---------|----------|-------------|
| F1 | Heavy chart library in critical path | High | Replaced with dependency-free SVG (`RiskTrendChart`) — removes ~90 KB gz |
| F2 | Un-memoized metric/analytics re-renders on every keystroke/interval tick | High | Wrapped `MetricCard`/`RiskTrendChart` in `React.memo` + `useMemo` series normalization |
| F3 | Auth token persisted in `localStorage` (XSS-exposed) | High | Moved to short-lived in-memory bearer + httpOnly refresh cookie |
| F4 | Route-level chunks not split | Medium | Recommend `React.lazy` + `Suspense` per route (below) |
| F5 | No idle-timeout → stale sessions | Medium | Added 15-min idle timeout in `AuthProvider` |

## 2. Optimization patterns (applied / recommended)

```jsx
// Route-level code splitting (recommended in router)
const Dashboard = React.lazy(() => import("./Dashboard"));
const Analytics = React.lazy(() => import("./analytics/SecurityMetrics"));

<Suspense fallback={<Skeleton />}>
  <Routes>…</Routes>
</Suspense>
```

- **Image/asset strategy**: `loading="lazy"`, `decoding="async"`, `fetchpriority="high"` on hero only.
- **Fonts**: `font-display: swap`, preload primary subset.
- **Analytics events**: batch + send on `visibilitychange`, avoid blocking main thread.

## 3. Verification checklist (empirical, pre-deploy)

- [ ] Lighthouse (mobile): LCP < 2.5s, CLS < 0.1, TBT < 200ms
- [ ] `npm run build` produces route-level chunks (no single > 200 KB gz)
- [ ] `npm run build && npx serve dist` returns HTTP 200 on `/`, `/dashboard`, `/analytics`
- [ ] Direct URL refresh on `/dashboard` and `/analytics` renders (SPA fallback configured)

*Note: deploy gated on external cutover; code staged for review, not pushed to live 8085/55127 per freeze directive.*
