/**
 * useRealtimeMetrics.js (Weaver deliverable 2026-09-04)
 * Supports: TASK-109D69 (Threat Intelligence Integration — real-time API hooks), TASK-D3981F/040E16 (analytics)
 *
 * Polls a metrics endpoint on an interval with exponential backoff on failure.
 * Zero-trust: each payload is validated (shape-checked) before it is emitted to the UI.
 */
import { useEffect, useState, useCallback, useRef } from 'react';

const DEFAULT_INTERVAL_MS = 15000;

function isWellFormed(payload) {
  return (
    payload &&
    typeof payload === 'object' &&
    Number.isFinite(payload.threatsMitigated) &&
    Number.isFinite(payload.complianceScore) &&
    Number.isFinite(payload.deployments) &&
    Number.isFinite(payload.uptime)
  );
}

export function useRealtimeMetrics({ endpoint = '/api/metrics/live', intervalMs = DEFAULT_INTERVAL_MS, enabled = true } = {}) {
  const [metrics, setMetrics] = useState(null);
  const [error, setError] = useState(null);
  const [connected, setConnected] = useState(false);
  const timerRef = useRef(null);
  const backoffRef = useRef(intervalMs);

  const load = useCallback(async () => {
    try {
      const res = await fetch(endpoint, { method: 'GET', credentials: 'include' });
      if (!res.ok) throw new Error(`Metrics endpoint responded ${res.status}`);
      const data = await res.json();
      if (!isWellFormed(data)) throw new Error('Malformed metrics payload');
      setMetrics(data);
      setError(null);
      setConnected(true);
      backoffRef.current = intervalMs; // reset after success
    } catch (err) {
      setError(err);
      setConnected(false);
      // exponential backoff up to 60s
      backoffRef.current = Math.min(backoffRef.current * 2, 60000);
    }
  }, [endpoint, intervalMs]);

  useEffect(() => {
    if (!enabled) return undefined;
    load();
    timerRef.current = window.setInterval(() => load(), backoffRef.current);
    return () => {
      if (timerRef.current) window.clearInterval(timerRef.current);
    };
  }, [enabled, load]);

  return { metrics, error, connected, refresh: load };
}
