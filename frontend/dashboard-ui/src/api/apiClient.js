/**
 * apiClient.js — Secure Dashboard API Integration Layer (Weaver deliverable 2026-09-04)
 * Supports: TASK-C3F879 (API Integration Layer — Secure Service Catalog Endpoints)
 *
 * Zero-trust client conventions:
 *  - credentials: 'include' (httpOnly session cookie; never tokens in JS storage)
 *  - CSRF token read from a server-set <meta> and echoed on mutating requests
 *  - response shape validation before emitting to UI (trust nothing by default)
 *  - AbortController timeouts so slow/stale endpoints never freeze the dashboard
 */
const DEFAULTS = {
  basePath: '/api',
  timeoutMs: 12000,
};

function readCsrfToken() {
  const meta = document.querySelector('meta[name="csrf-token"]');
  return meta ? meta.getAttribute('content') : '';
}

function validateProductShape(payload) {
  return (
    Array.isArray(payload?.products) &&
    payload.products.every(
      (p) => p && typeof p === 'object' && typeof p.id === 'string' && typeof p.name === 'string',
    )
  );
}

export class ApiClient {
  constructor(options = {}) {
    this.basePath = options.basePath || DEFAULTS.basePath;
    this.timeoutMs = options.timeoutMs || DEFAULTS.timeoutMs;
  }

  async request(path, { method = 'GET', body, signal } = {}) {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), this.timeoutMs);
    const externalSignal = signal;
    const onAbort = () => ctrl.abort();
    if (externalSignal) {
      if (externalSignal.aborted) ctrl.abort();
      else externalSignal.addEventListener('abort', onAbort);
    }
    try {
      const headers = { Accept: 'application/json' };
      if (body !== undefined) {
        headers['Content-Type'] = 'application/json';
        headers['X-CSRF-Token'] = readCsrfToken();
      }
      const res = await fetch(`${this.basePath}${path}`, {
        method,
        headers,
        credentials: 'include',
        body: body !== undefined ? JSON.stringify(body) : undefined,
        signal: ctrl.signal,
      });
      if (!res.ok) {
        const err = new Error(`Request failed (${res.status})`);
        err.status = res.status;
        throw err;
      }
      return await res.json();
    } finally {
      clearTimeout(timer);
      if (externalSignal) externalSignal.removeEventListener('abort', onAbort);
    }
  }

  /** Service catalog — customer-facing product list */
  async getCatalogProducts() {
    const payload = await this.request('/catalog/products');
    if (!validateProductShape(payload)) {
      throw new Error('Catalog endpoint returned an unexpected payload shape.');
    }
    return payload.products;
  }

  /** Session re-verification (zero trust: never trust cached state) */
  async verifySession() {
    const payload = await this.request('/auth/session');
    if (!payload || typeof payload !== 'object') {
      throw new Error('Session endpoint returned an unexpected payload.');
    }
    return payload.user || null;
  }

  /** Contact / inquiry submission used by dashboard support surfaces */
  async submitInquiry({ name, email, message, topic }) {
    const payload = await this.request('/contact', {
      method: 'POST',
      body: { name, email, message, topic },
    });
    if (!payload || payload.ok !== true) {
      throw new Error('Inquiry submission was not acknowledged.');
    }
    return payload;
  }
}

export const apiClient = new ApiClient();
export default apiClient;
