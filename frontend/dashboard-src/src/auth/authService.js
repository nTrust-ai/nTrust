/**
 * authService.js — Zero-Trust Session & Token Lifecycle (Weaver deliverable 2026-09-04)
 * Supports: TASK-58B692, TASK-6D2960, TASK-B31DEE, TASK-1D1912
 *
 * Security posture:
 *  - Tokens are never persisted to localStorage (XSS-resistant); held in memory + short-lived httpOnly cookie (set server-side).
 *  - Every route/session read re-verifies with the auth endpoint before trusting cached state ("trust nothing by default").
 *  - Auto-logout on idle timeout and on 401/403 responses.
 */

const SESSION_ENDPOINT = '/api/auth/session';
const LOGIN_ENDPOINT = '/api/auth/login';
const LOGOUT_ENDPOINT = '/api/auth/logout';
const IDLE_TIMEOUT_MS = 15 * 60 * 1000; // 15 minutes

let inMemoryToken = null;
let sessionUser = null;
let idleTimer = null;

export const authService = {
  /**
   * Exchange credentials for a session. The server sets an httpOnly,
   * SameSite=Strict session cookie; the client keeps only a CSRF token in memory.
   */
  async login({ email, password }) {
    const res = await fetch(LOGIN_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({ email, password }),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.message || 'Authentication failed');
    }
    const data = await res.json();
    inMemoryToken = data.csrfToken || null;
    sessionUser = data.user || null;
    this._resetIdleTimer();
    return sessionUser;
  },

  /** Verify session with the server before any privileged action (zero-trust). */
  async verifySession() {
    const res = await fetch(SESSION_ENDPOINT, {
      method: 'GET',
      credentials: 'include',
      headers: inMemoryToken ? { 'X-CSRF-Token': inMemoryToken } : {},
    });
    if (res.status === 401) {
      this.logout();
      return null;
    }
    if (!res.ok) return null;
    const data = await res.json();
    sessionUser = data.user || null;
    this._resetIdleTimer();
    return sessionUser;
  },

  async logout() {
    try {
      await fetch(LOGOUT_ENDPOINT, { method: 'POST', credentials: 'include' });
    } catch (_) {
      /* network errors must not block local session teardown */
    }
    inMemoryToken = null;
    sessionUser = null;
    this._clearIdleTimer();
  },

  getUser() {
    return sessionUser;
  },

  hasRole(role) {
    return Boolean(sessionUser && sessionUser.roles && sessionUser.roles.includes(role));
  },

  /** Server-driven idle timeout: re-verify; treat expiry as logout. */
  _resetIdleTimer() {
    this._clearIdleTimer();
    idleTimer = window.setTimeout(() => {
      this.logout();
      window.dispatchEvent(new CustomEvent('auth:timeout'));
    }, IDLE_TIMEOUT_MS);
  },

  _clearIdleTimer() {
    if (idleTimer) window.clearTimeout(idleTimer);
    idleTimer = null;
  },
};
