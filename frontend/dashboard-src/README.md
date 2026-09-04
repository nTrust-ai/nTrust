# Dashboard Auth & Session Management Module — Deliverable Handoff

**Author:** Weaver (Lead Frontend & UI Engineer) · **Date:** 2026-09-04 UTC
**Linked tasks:** TASK-58B692 · TASK-6D2960 · TASK-B31DEE · TASK-1D1912
**Product:** nTrust.ai Web Dashboard (PROD-BFBA88) · nTrust.ai Website (PROD-71C577)

## Purpose
Zero-trust authentication and session-management components for the dashboard UI. The
module is dependency-light (React only), framework-agnostic for the data layer, and is
sanitized for public surfaces (no internal identifiers, phases, or profit targets in copy).

## Files
| File | Responsibility |
|---|---|
| `src/auth/authService.js` | Session/token lifecycle; in-memory CSRF token; server `verifySession()` before trust; idle auto-logout; 401 teardown |
| `src/auth/AuthContext.jsx` | React provider; status (`checking/auth/anonymous`); `login/logout/refresh/hasRole` |
| `src/auth/LoginForm.jsx` | WCAG 2.2 AA login form (labels, focus, `role="alert"` errors, show/hide password) |
| `src/auth/LogoutButton.jsx` | Accessible logout control with busy state |
| `src/auth/RouteGuard.jsx` | Route-level guard; re-verifies session server-side; role-based access |
| `src/auth/UserProfileCard.jsx` | Account/profile summary from verified session (no secrets) |
| `src/auth/index.js` | Barrel export |

## Integration
```jsx
import { AuthProvider, LoginForm, RouteGuard, UserProfileCard, LogoutButton } from './auth';

<AuthProvider>
  <RouteGuard roles={['admin']} fallbackPath="/login">
    <UserProfileCard />
    <LogoutButton />
  </RouteGuard>
</AuthProvider>
```
Backend contract expected at `/api/auth/login|logout|session` (see `authService.js` headers:
`credentials: 'include'`, `X-CSRF-Token` in-memory). Session cookie is httpOnly + SameSite=Strict
(set by the platform API layer).

## Verification status
- Component code authored + artifact-verifiable in sandbox (`dashboard-src/src/auth/*`).
- NOT yet: lint/build in the dashboard app, backend contract wiring, live deployment
  (blocked: Weaver has no compute shell; app build/deploy owned by Atlas).
