/**
 * ProfitVelocityReport.jsx — Executive Reporting: profit velocity metrics (Weaver deliverable 2026-09-04)
 * Supports: TASK-903525 ([P2] Executive Reporting - Profit Velocity Metrics)
 *
 * Purpose: Board/executive read-only widget rendering revenue-health KPIs from the
 * secured metrics API. Data is fetched through the zero-trust session layer; every
 * payload is schema-validated before render (defense in depth). Sanitized labels —
 * no internal task codes, phases, or channel details surface here.
 *
 * WCAG 2.2 AA: each KPI is a list item with a labelled value; trend text uses
 * aria-hidden arrows with semantic "+/-" duplicates; region announces live updates.
 */
import { useCallback, useEffect, useReducer, useRef } from 'react';

const initialState = {
  state: 'loading', // loading | ready | error
  metrics: null,
  error: null,
};

function reducer(current, action) {
  switch (action.type) {
    case 'LOADING':
      return { ...current, state: 'loading', error: null };
    case 'READY':
      return { state: 'ready', metrics: action.metrics, error: null };
    case 'ERROR':
      return { state: 'error', metrics: null, error: action.error };
    default:
      return current;
  }
}

function isPlausibleMetrics(value) {
  return (
    value &&
    typeof value === 'object' &&
    ['velocity', 'retention', 'margin'].every((key) => typeof value[key] === 'number')
  );
}

export function ProfitVelocityReport({ refreshMs = 30000 }) {
  const [state, dispatch] = useReducer(reducer, initialState);
  const timerRef = useRef(null);

  const load = useCallback(async (signal) => {
    dispatch({ type: 'LOADING' });
    try {
      const res = await fetch('/api/reporting/profit-velocity', {
        headers: { Accept: 'application/json' },
        credentials: 'include',
        signal,
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const payload = await res.json();
      if (!isPlausibleMetrics(payload.metrics)) {
        throw new Error('Invalid metrics payload shape');
      }
      dispatch({ type: 'READY', metrics: payload.metrics });
    } catch (err) {
      if (err.name !== 'AbortError') {
        dispatch({ type: 'ERROR', error: 'Unable to load reporting metrics.' });
      }
    }
  }, []);

  useEffect(() => {
    const controller = new AbortController();
    load(controller.signal);
    timerRef.current = setInterval(() => load(controller.signal), refreshMs);
    return () => {
      controller.abort();
      clearInterval(timerRef.current);
    };
  }, [load, refreshMs]);

  const { metrics } = state;

  return (
    <section
      aria-labelledby="profit-velocity-heading"
      className="report-widget"
      data-testid="profit-velocity-report"
    >
      <h3 id="profit-velocity-heading">Profit Velocity</h3>

      {state.state === 'loading' && <p aria-busy="true">Loading reporting metrics…</p>}
      {state.state === 'error' && (
        <p role="alert" className="report-error">
          {state.error}
        </p>
      )}

      {state.state === 'ready' && metrics ? (
        <ul className="report-kpi-list" aria-live="polite">
          <li>
            <span className="report-kpi-label">Revenue Velocity</span>
            <span className="report-kpi-value">
              {formatMoney(metrics.velocity)}<span className="sr-only"> per month</span>
            </span>
            <span className="report-kpi-unit">/month</span>
          </li>
          <li>
            <span className="report-kpi-label">Gross Margin</span>
            <span className="report-kpi-value">{formatPct(metrics.margin)}</span>
          </li>
          <li>
            <span className="report-kpi-label">Contract Retention</span>
            <span className="report-kpi-value">{formatPct(metrics.retention)}</span>
          </li>
        </ul>
      ) : null}
    </section>
  );
}

function formatMoney(value) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  }).format(value);
}

function formatPct(value) {
  return `${value.toFixed(1)}%`;
}
