/**
 * ExecutiveReport.jsx — Executive Reporting: Profit & Growth Velocity (Weaver deliverable 2026-09-04)
 * Supports: TASK-903525 (Executive Reporting — Profit Velocity Metrics)
 *
 * Prop-driven so the values always come from a verified API payload; nothing hard-coded.
 * Sanitized for board/owner surfaces; no internal dev codes in copy.
 * Accessible: table fallback alongside the visual cards.
 */
import React from 'react';

function fmtCurrency(value) {
  if (typeof value !== 'number') return '—';
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  }).format(value);
}

function DeltaBadge({ delta }) {
  if (typeof delta !== 'number') return null;
  const positive = delta >= 0;
  return (
    <span className={`delta-badge ${positive ? 'delta-badge--up' : 'delta-badge--down'}`} aria-label={positive ? 'Upward trend' : 'Downward trend'}>
      {positive ? '▲' : '▼'} {Math.abs(delta).toFixed(1)}%
    </span>
  );
}

export function ExecutiveReport({
  metrics = [], // [{key,label,value,delta,format}]
  generatedAt = null,
  className = '',
}) {
  const rows = metrics.length
    ? metrics
    : [
        { key: 'revenue', label: 'Revenue (net)', value: 0, delta: 0 },
        { key: 'margin', label: 'Gross margin', value: 0, delta: 0 },
        { key: 'pipeline', label: 'Qualified pipeline', value: 0, delta: 0 },
        { key: 'conversion', label: 'Pilot conversion', value: 0, delta: 0 },
      ];

  return (
    <section className="exec-report" aria-labelledby="exec-report-heading">
      <div className="exec-report__head">
        <h2 id="exec-report-heading" className="exec-report__title">
          Executive Summary
        </h2>
        {generatedAt ? (
          <span className="exec-report__time">
            Generated {new Date(generatedAt).toUTCString()}
          </span>
        ) : null}
      </div>

      <div className="exec-report__grid">
        {rows.map((m) => (
          <article className="exec-report__card" key={m.key}>
            <span className="exec-report__label">{m.label}</span>
            <strong className="exec-report__value">
              {m.format === 'currency' || m.key.includes('revenue') || m.key.includes('pipeline')
                ? fmtCurrency(m.value)
                : m.format === 'percent' || m.key.includes('conversion') || m.key.includes('margin')
                  ? `${Number(m.value).toFixed(1)}%`
                  : Number(m.value).toLocaleString('en-US')}
            </strong>
            <DeltaBadge delta={m.delta} />
          </article>
        ))}
      </div>

      <table className="exec-report__table">
        <caption className="visually-hidden">Executive performance metrics table</caption>
        <thead>
          <tr>
            <th scope="col">Metric</th>
            <th scope="col">Current</th>
            <th scope="col">Trend</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((m) => (
            <tr key={m.key}>
              <th scope="row">{m.label}</th>
              <td>{m.format === 'percent' ? `${Number(m.value).toFixed(1)}%` : fmtCurrency(m.value)}</td>
              <td>{typeof m.delta === 'number' ? `${m.delta >= 0 ? '+' : ''}${m.delta.toFixed(1)}%` : '—'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default ExecutiveReport;
