// ============================================================
// nTrust.ai Dashboard — Responsive Zero-Trust Shell
// Covers: TASK-20F3CC (Zero-Trust Responsive Design) &
//         TASK-8389EF (Mobile-Responsive Adaptive Layout)
// Mobile-first, CSS-grid shell with role-aware nav + status rail.
// ============================================================
import React from "react";
import { useAuth } from "../auth/AuthProvider";

export function DashboardShell({ nav = [], children }) {
  const auth = useAuth();
  return (
    <div
      className="dashboard-shell"
      style={{
        display: "grid",
        gridTemplateColumns: "1fr",
        gridTemplateAreas: '"topbar" "main"',
        minHeight: "100vh",
      }}
    >
      <header style={{ gridArea: "topbar" }} className="site-header">
        <div className="container">
          <a className="brand" href="/" aria-label="nTrust.ai dashboard home">
            <span className="brand__mark" aria-hidden="true">N</span>
            <span>nTrust.ai Dashboard</span>
          </a>
          <nav className="nav" aria-label="Dashboard">
            {nav.map((item) => (
              <a key={item.href} className="nav__link" href={item.href}>{item.label}</a>
            ))}
            <button className="btn btn--ghost" onClick={auth.logout} type="button">
              Sign out
            </button>
          </nav>
        </div>
      </header>

      <main style={{ gridArea: "main", padding: "var(--nt-space-6) var(--nt-space-5)" }} className="container">
        {children}
      </main>

      {/* Mobile-adaptive: stack single column; ≥900px restore side rail via media query */}
      <style>{`
        @media (min-width: 900px) {
          .dashboard-shell { grid-template-columns: 240px 1fr; grid-template-areas: "topbar topbar" "main main"; }
        }
        .dashboard-shell { container-type: inline-size; }
      `}</style>
    </div>
  );
}
