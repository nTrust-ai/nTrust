/**
 * DashboardLayout.jsx — Zero-Trust Responsive Dashboard Shell (Weaver deliverable 2026-09-04)
 * Supports: TASK-20F3CC (Dashboard Layout — Zero-Trust Responsive Design), TASK-42642E
 * (Core Layout & Navigation), TASK-8389EF (Mobile-Responsive Design), TASK-B99044 (Web Dashboard MVP)
 *
 * - Landmarks: skip link, header, nav, main — WCAG 2.2 AA.
 * - Zero-trust posture surfacing: session state chip; content never trusted until verified (handled by auth layer).
 * - Responsive: sidebar collapses to overlay drawer under 960px; topbar condenses; touch targets >= 44px.
 */
import React, { useEffect, useRef, useState } from 'react';
import './dashboard.css';

const DEFAULTS = {
  brand: 'nTrust.ai',
  navItems: [
    { key: 'overview', label: 'Overview', href: '#overview' },
    { key: 'analytics', label: 'Analytics', href: '#analytics' },
    { key: 'threats', label: 'Threat Intelligence', href: '#threats' },
    { key: 'strategy', label: 'Strategy', href: '#strategy' },
    { key: 'reports', label: 'Reports', href: '#reports' },
    { key: 'settings', label: 'Settings', href: '#settings' },
  ],
};

function useMediaQuery(query) {
  const [matches, setMatches] = useState(() =>
    typeof window !== 'undefined' ? window.matchMedia(query).matches : false,
  );
  useEffect(() => {
    const mql = window.matchMedia(query);
    const onChange = (e) => setMatches(e.matches);
    mql.addEventListener('change', onChange);
    setMatches(mql.matches);
    return () => mql.removeEventListener('change', onChange);
  }, [query]);
  return matches;
}

export function DashboardLayout({
  brand = DEFAULTS.brand,
  navItems = DEFAULTS.navItems,
  activeKey = 'overview',
  onNavigate,
  user,
  onLogout,
  sessionStatus = 'authenticated', // checking | authenticated | anonymous
  children,
  footer = null,
}) {
  const isDesktop = useMediaQuery('(min-width: 960px)');
  const [navOpen, setNavOpen] = useState(false);
  const mainRef = useRef(null);

  // Close the mobile drawer when resizing up to desktop
  useEffect(() => {
    if (isDesktop) setNavOpen(false);
  }, [isDesktop]);

  function handleNav(item) {
    setNavOpen(false);
    if (onNavigate) onNavigate(item);
  }

  const statusLabel =
    sessionStatus === 'checking'
      ? 'Verifying session…'
      : sessionStatus === 'authenticated'
        ? 'Secure session active'
        : 'Session required';

  return (
    <div className={`ntrust-shell ${navOpen ? 'ntrust-shell--nav-open' : ''}`}>
      <a className="ntrust-skip-link" href="#ntrust-main">
        Skip to main content
      </a>

      <header className="ntrust-topbar">
        <button
          type="button"
          className="ntrust-menu-toggle"
          aria-expanded={navOpen}
          aria-controls="ntrust-nav"
          aria-label={navOpen ? 'Close navigation' : 'Open navigation'}
          onClick={() => setNavOpen((v) => !v)}
        >
          <span className="ntrust-menu-toggle__bar" />
          <span className="ntrust-menu-toggle__bar" />
          <span className="ntrust-menu-toggle__bar" />
        </button>

        <a className="ntrust-brand" href="#overview">
          {brand}
        </a>

        <div className="ntrust-topbar__spacer" />

        <span className="ntrust-session-chip" role="status">
          <span
            className={`ntrust-session-chip__dot ntrust-session-chip__dot--${sessionStatus}`}
            aria-hidden="true"
          />
          {statusLabel}
        </span>

        {user ? (
          <div className="ntrust-user">
            <span className="ntrust-user__name">{user.name || user.email || 'Account'}</span>
            {onLogout && (
              <button type="button" className="ntrust-btn ntrust-btn--ghost" onClick={onLogout}>
                Sign out
              </button>
            )}
          </div>
        ) : null}
      </header>

      <div className="ntrust-body">
        {isDesktop ? (
          <nav className="ntrust-nav" aria-label="Primary">
            {navItems.map((item) => (
              <a
                key={item.key}
                href={item.href}
                aria-current={item.key === activeKey ? 'page' : undefined}
                className={`ntrust-nav__link ${item.key === activeKey ? 'ntrust-nav__link--active' : ''}`}
                onClick={() => handleNav(item)}
              >
                {item.label}
              </a>
            ))}
          </nav>
        ) : (
          <div className="ntrust-drawer-backdrop" onClick={() => setNavOpen(false)} aria-hidden="true" />
        )}

        <nav
          id="ntrust-nav"
          className={`ntrust-drawer ${navOpen ? 'ntrust-drawer--open' : ''}`}
          aria-label="Primary"
          aria-hidden={!navOpen}
        >
          <div className="ntrust-drawer__brand">{brand}</div>
          {navItems.map((item) => (
            <a
              key={item.key}
              href={item.href}
              aria-current={item.key === activeKey ? 'page' : undefined}
              tabIndex={navOpen ? 0 : -1}
              className={`ntrust-nav__link ${item.key === activeKey ? 'ntrust-nav__link--active' : ''}`}
              onClick={() => handleNav(item)}
            >
              {item.label}
            </a>
          ))}
        </nav>

        <main id="ntrust-main" className="ntrust-main" ref={mainRef} tabIndex={-1}>
          {children}
        </main>
      </div>

      {footer ? <footer className="ntrust-footer">{footer}</footer> : null}
    </div>
  );
}

export default DashboardLayout;
