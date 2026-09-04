/**
 * endpoints.js — Centralized secure service-catalog endpoint registry (Weaver deliverable 2026-09-04)
 * Supports: TASK-C3F879 ([PHASE 3] API Integration Layer — Secure Service Catalog Endpoints)
 *
 * Single source of truth for dashboard API paths. All consumers import from here so the
 * platform layer can remap versions/proxies without touching feature code.
 */
export const ENDPOINTS = {
  // Auth & session (auth/)
  login: '/api/auth/login',
  logout: '/api/auth/logout',
  session: '/api/auth/session',

  // Realtime security metrics (viz/)
  metricsLive: '/api/metrics/live',
  analyzerPosture: '/api/analyzer/posture',

  // Product/service catalog endpoints (public-facing, sanitized)
  catalog: '/api/catalog',
  productDetail: (slug) => `/api/catalog/products/${encodeURIComponent(slug)}`,
  serviceDetail: (slug) => `/api/catalog/services/${encodeURIComponent(slug)}`,

  // SUN-token early access (sunToken/)
  sunTokenEarlyAccess: '/api/sun-token/early-access',

  // Executive reporting (reporting/)
  profitVelocity: '/api/reporting/profit-velocity',
};

export const productSlugs = [
  'trustguard',
  'trustaudit-engine',
  'sun-token',
  'ntrust-core',
  'privacyguard',
  'ntrust-shield',
];
