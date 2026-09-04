/**
 * DashboardApp.jsx — nTrust.ai Customer Dashboard shell (Weaver 2026-09-04)
 * Zero-trust navigation shell. Routes behind RouteGuard where sessions are required.
 * WCAG 2.2 AA: semantic landmarks, skip-link, visible focus, live regions.
 * Supports: TASK-20F3CC · TASK-42642E · TASK-B99044 · TASK-8389EF · TASK-58B692 ·
 *           TASK-6D2960 · TASK-B31DEE · TASK-1D1912 · TASK-C3F879 · TASK-D3981F ·
 *           TASK-040E16 · TASK-D29780 · TASK-109D69 · TASK-E6231D · TASK-35AE4C ·
 *           TASK-903525 · TASK-766348 · TASK-BFF3F9
 */
import React, { lazy, Suspense, useMemo, useState } from 'react';
import { Routes, Route, NavLink, Navigate } from 'react-router-dom';
import { useAuth, LoginForm, LogoutButton, RouteGuard, UserProfileCard } from '../auth';
import { SecurityMetricsPanel, ThreatFeed, StrategyWidget } from '../viz';

// Perf: route-level code splitting keeps the initial bundle lean.
const ThreatTimeline = lazy(() => import('../viz/ThreatTimeline').then((m) => ({ default: m.ThreatTimeline })));
const ProfitVelocityReport = lazy(() => import('../reporting/ProfitVelocityReport').then((m) => ({ default: m.ProfitVelocityReport })));
const SunTokenCard = lazy(() => import('../sunToken/SunTokenCard').then((m) => ({ default: m.SunTokenCard })));

const NAV_ITEMS = [
  { to: '/', label: 'Overview', end: true },
  { to: '/intelligence', label: 'Threat Intelligence' },
  { to: '/reporting', label: 'Executive Reporting' },
  { to: '/sun-token', label: 'SUN-token' }
];

function SkipLink() {
  return <a className="skip-link" href="#main-content">Skip to main content</a>;
}

function AppNav() {
  return (
    <nav aria-label="Primary" className="app-nav">
      {NAV_ITEMS.map((item) => (
        <NavLink
          key={item.to}
          to={item.to}
          end={item.end}
          className={({ isActive }) => (isActive ? 'nav-link nav-link--active' : 'nav-link')}
        >
          {item.label}
        </NavLink>
      ))}
    </nav>
  );
}

function OverviewPage() {
  const { user } = useAuth();
  return (
    <section aria-label="Security overview">
      <div className="kpi-grid">
        <SecurityMetricsPanel />
        <div className="panel">
          <h2>Security posture</h2>
          <StrategyWidget />
        </div>
      </div>
      <div className="panel">
        <h2>Live threat feed</h2>
        <ThreatFeed limit={8} />
      </div>
      {user && (
        <div className="panel">
          <h2>Account</h2>
          <UserProfileCard user={user} />
        </div>
      )}
    </section>
  );
}

function SecureFallback() {
  return (
    <div className="panel" role="status" aria-live="polite">
      <h2>Loading…</h2>
      <p>Preparing your secure view.</p>
    </div>
  );
}

export function DashboardApp() {
  const { sessionReady } = useAuth();
  const [menuOpen, setMenuOpen] = useState(false);
  const todayLabel = useMemo(
    () => new Date().toISOString().slice(0, 10),
    []
  );

  if (!sessionReady) {
    return (
      <div className="auth-screen">
        <header className="auth-header">
          <span className="brand">nTrust.ai</span>
        </header>
        <main className="auth-main" id="main-content">
          <LoginForm />
        </main>
      </div>
    );
  }

  return (
    <>
      <SkipLink />
      <header className="app-header">
        <NavLink to="/" className="brand">nTrust.ai</NavLink>
        <button
          type="button"
          className="menu-toggle"
          aria-expanded={menuOpen}
          aria-controls="primary-nav"
          onClick={() => setMenuOpen((v) => !v)}
        >
          Menu
        </button>
        <div id="primary-nav" className={menuOpen ? 'nav-wrap nav-wrap--open' : 'nav-wrap'}>
          <AppNav />
          <LogoutButton />
        </div>
      </header>
      <main id="main-content" className="app-main">
        <Routes>
          <Route path="/" element={<OverviewPage />} />
          <Route
            path="/intelligence"
            element={
              <RouteGuard>
                <Suspense fallback={<SecureFallback />}>
                  <section aria-label="Threat intelligence">
                    <h1>Threat intelligence</h1>
                    <ThreatTimeline />
                  </section>
                </Suspense>
              </RouteGuard>
            }
          />
          <Route
            path="/reporting"
            element={
              <RouteGuard>
                <Suspense fallback={<SecureFallback />}>
                  <ProfitVelocityReport asOf={todayLabel} />
                </Suspense>
              </RouteGuard>
            }
          />
          <Route
            path="/sun-token"
            element={
              <Suspense fallback={<SecureFallback />}>
                <SunTokenCard />
              </Suspense>
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
      <footer className="app-footer">
        <span>nTrust.ai — Autonomous security &amp; compliance.</span>
      </footer>
    </>
  );
}
