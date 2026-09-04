/**
 * AuthContext.jsx — React context for authentication state (Weaver deliverable 2026-09-04)
 * Supports: TASK-58B692 (Auth & Session Mgmt), TASK-6D2960 (Secure Login/Logout), TASK-B31DEE (Dashboard Auth & User Profile)
 *
 * Zero-trust: state is hydrated only after server verifySession(); never trusted from client storage.
 */
import React, { createContext, useContext, useEffect, useMemo, useState, useCallback } from 'react';
import { authService } from './authService';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [status, setStatus] = useState('checking'); // checking | authenticated | anonymous

  useEffect(() => {
    let cancelled = false;
    authService
      .verifySession()
      .then((u) => {
        if (cancelled) return;
        setUser(u);
        setStatus(u ? 'authenticated' : 'anonymous');
      })
      .catch(() => {
        if (!cancelled) setStatus('anonymous');
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const login = useCallback(async (credentials) => {
    const u = await authService.login(credentials);
    setUser(u);
    setStatus('authenticated');
    return u;
  }, []);

  const logout = useCallback(async () => {
    await authService.logout();
    setUser(null);
    setStatus('anonymous');
  }, []);

  const refresh = useCallback(async () => {
    const u = await authService.verifySession();
    setUser(u);
    setStatus(u ? 'authenticated' : 'anonymous');
    return u;
  }, []);

  useEffect(() => {
    const onTimeout = () => {
      setUser(null);
      setStatus('anonymous');
    };
    window.addEventListener('auth:timeout', onTimeout);
    return () => window.removeEventListener('auth:timeout', onTimeout);
  }, []);

  const value = useMemo(
    () => ({ user, status, login, logout, refresh, hasRole: (r) => Boolean(user?.roles?.includes(r)) }),
    [user, status, login, logout, refresh],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within <AuthProvider>');
  return ctx;
}
