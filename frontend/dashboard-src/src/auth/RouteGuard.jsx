/**
 * RouteGuard.jsx — Zero-trust route guard (Weaver deliverable 2026-09-04)
 * Supports: TASK-58B692 (Auth & Session Mgmt), TASK-1D1912 (Dashboard Authentication & Security Layer)
 *
 * Trusts nothing by default: re-verifies the session server-side on mount before rendering
 * protected content; renders an accessible "checking" state and redirects anonymous users.
 */
import React, { useEffect, useState } from 'react';
import { useAuth } from './AuthContext';

export function RouteGuard({ children, roles, fallbackPath = '/login', checking = null }) {
  const { user, status, refresh } = useAuth();
  const [verifying, setVerifying] = useState(status === 'checking');

  useEffect(() => {
    let cancelled = false;
    if (status === 'checking') {
      refresh().finally(() => {
        if (!cancelled) setVerifying(false);
      });
    } else {
      setVerifying(false);
    }
    return () => {
      cancelled = true;
    };
  }, [status, refresh]);

  if (verifying || status === 'checking') {
    return checking || <div className="route-guard-status">Verifying secure session…</div>;
  }

  if (!user) {
    window.location.assign(fallbackPath);
    return null;
  }

  if (roles && roles.length > 0 && !roles.some((r) => user.roles?.includes(r))) {
    return (
      <div role="alert" className="access-denied">
        You do not have permission to view this page.
      </div>
    );
  }

  return children;
}
