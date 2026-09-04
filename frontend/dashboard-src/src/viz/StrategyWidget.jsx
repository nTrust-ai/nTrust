/**
 * StrategyWidget.jsx (Weaver deliverable 2026-09-04)
 * Supports: TASK-E6231D (AI Security Strategy Analyzer — dashboard widget)
 *
 * Renders posture recommendations returned by the analyzer API. Kept deliberately
 * professional and sanitized (no internal targets/codes) for customer-visible dashboard.
 */
import React, { useEffect, useState } from 'react';

export function StrategyWidget({ endpoint = '/api/analyzer/posture', className = '' }) {
  const [state, setState] = useState({ loading: true, items: [], error: null });

  useEffect(() => {
    let cancelled = false;
    fetch(endpoint, { credentials: 'include' })
      .then((res) => {
        if (!res.ok) throw new Error('Analyzer unavailable');
        return res.json();
      })
      .then((data) => {
        if (!cancelled) setState({ loading: false, items: Array.isArray(data.recommendations) ? data.recommendations : [], error: null });
      })
      .catch((err) => {
        if (!cancelled) setState({ loading: false, items: [], error: err.message });
      });
    return () => {
      cancelled = true;
    };
  }, [endpoint]);

  return (
    <section aria-label="Security strategy" className={`strategy-widget ${className}`}>
      <h2>Posture Strategy</h2>
      {state.loading ? <p>Analyzing posture…</p> : null}
      {state.error ? <p role="alert">{state.error}</p> : null}
      {!state.loading && !state.error ? (
        <ul className="strategy-list">
          {state.items.map((item) => (
            <li key={item.id} className={`strategy-item priority-${item.priority || 'low'}`}>
              <p className="strategy-title">{item.title}</p>
              <p className="strategy-desc">{item.description}</p>
            </li>
          ))}
        </ul>
      ) : null}
    </section>
  );
}
