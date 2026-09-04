/**
 * client.js — Secure API client core (Weaver deliverable 2026-09-04)
 * Supports: TASK-C3F879 ([PHASE 3] API Integration Layer — Secure Service Catalog Endpoints)
 *
 * Zero-trust fetch wrapper used by every dashboard module:
 *  - httpOnly session cookies (credentials: 'include') + in-memory CSRF header
 *  - AbortController timeouts so UI never hangs on a dead endpoint
 *  - bounded retry w/ exponential backoff for idempotent GETs only
 *  - central JSON error normalization (no stack/leak to UI)
 */
const DEFAULT_TIMEOUT_MS = 8000;
const MAX_RETRIES = 2;

export class ApiError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
  }
}

function csrfToken() {
  // In-memory token issued by the platform auth layer; never persisted to storage.
  return window.__NTRUST_CSRF__ || '';
}

export async function apiRequest(path, { method = 'GET', body, timeoutMs = DEFAULT_TIMEOUT_MS, retries = 0 } = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const headers = { Accept: 'application/json' };
    if (body !== undefined) {
      headers['Content-Type'] = 'application/json';
    }
    const token = csrfToken();
    if (token) headers['X-CSRF-Token'] = token;

    const res = await fetch(path, {
      method,
      headers,
      credentials: 'include',
      signal: controller.signal,
      body: body === undefined ? undefined : JSON.stringify(body),
    });

    if (res.status === 401) {
      window.dispatchEvent(new CustomEvent('ntrust:session-expired'));
      throw new ApiError('Session expired. Please sign in again.', 401);
    }
    if (!res.ok) {
      const detail = await safeText(res);
      throw new ApiError(detail || `Request failed (${res.status})`, res.status);
    }
    if (res.status === 204) return null;
    return await res.json();
  } catch (err) {
    if (err.name === 'AbortError') throw new ApiError('Request timed out. Please retry.', 0);
    if (err instanceof ApiError) throw err;
    throw new ApiError('Network error. Please check your connection.', 0);
  } finally {
    clearTimeout(timer);
  }
}

export async function apiGet(path, options = {}) {
  const { retries = MAX_RETRIES, ...rest } = options;
  let attempt = 0;
  for (;;) {
    try {
      return await apiRequest(path, { method: 'GET', ...rest });
    } catch (err) {
      if (attempt >= retries || !isRetryable(err)) throw err;
      attempt += 1;
      await new Promise((r) => setTimeout(r, 250 * 2 ** attempt)); // exponential backoff
    }
  }
}

export async function apiPost(path, body, options = {}) {
  return apiRequest(path, { method: 'POST', body, ...options });
}

function isRetryable(err) {
  return err instanceof ApiError && (err.status === 0 || err.status >= 500);
}

async function safeText(res) {
  try {
    const data = await res.json();
    return data && data.message ? data.message : '';
  } catch {
    return '';
  }
}
