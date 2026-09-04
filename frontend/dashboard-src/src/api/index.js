/**
 * index.js — API Integration Layer barrel export (Weaver deliverable 2026-09-04)
 * Supports: TASK-C3F879 ([PHASE 3] API Integration Layer — Secure Service Catalog Endpoints)
 */
export { apiGet, apiPost, apiRequest, ApiError } from './client';
export { ENDPOINTS, productSlugs } from './endpoints';
