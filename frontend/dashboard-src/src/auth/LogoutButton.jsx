/**
 * LogoutButton.jsx (Weaver deliverable 2026-09-04) — TASK-6D2960 Secure Login/Logout Flow
 */
import React, { useState } from 'react';
import { useAuth } from './AuthContext';

export function LogoutButton({ className = '', redirectPath = '/login' }) {
  const { logout } = useAuth();
  const [busy, setBusy] = useState(false);

  async function handleLogout() {
    setBusy(true);
    try {
      await logout();
    } finally {
      setBusy(false);
      window.location.assign(redirectPath);
    }
  }

  return (
    <button
      type="button"
      className={className || 'btn btn-ghost'}
      onClick={handleLogout}
      disabled={busy}
      aria-busy={busy}
    >
      {busy ? 'Signing out…' : 'Sign out'}
    </button>
  );
}
