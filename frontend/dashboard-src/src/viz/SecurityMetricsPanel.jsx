/**
 * SecurityMetricsPanel.jsx (Weaver deliverable 2026-09-04)
 * Supports: TASK-D3981F (Dashboard Analytics — real-time security metrics), TASK-040E16
 *
 * Renders KPI cards from the live metrics hook with an accessible live region,
 * connection state, and trend deltas. No internal identifiers in copy.
 */
import React from 'react';
import { useRealtimeMetrics } from './useRealtimeMetrics';

function KpiCard({ label, value, delta, tone = 'neutral' }) {
  return (
    <article className={`kpi-card tone-${tone}`}>
      <h3 className="kpi-label">{label}</h3>
      <p className="kpi-value" data-testid={`kpi-${label}`}>{value}</p>
      {delta ? <p className="kpi-delta" aria-label={`${delta} versus prior period`}>{delta}</p> : null}
    </article>
  );
}

export function SecurityMetricsPanel({ className = '' }) {
  const { metrics, error, connected, refresh } = useRealtimeMetrics();

  return (
    <section aria-label="Live security metrics" className={`metrics-panel ${className}`}>
      <div className="panel-head">
        <h2>Live Platform Overview</h2>
        <span className={`conn-badge ${connected ? 'on' : 'off'}`} role="status">
          {connected ? 'Live' : 'Reconnecting'}
        </span>
      </div>
      {error ? (
        <p role="alert" className="form-error">
          Unable to refresh metrics. <button type="button" className="link-btn" onClick={refresh}>Retry</button>
        </p>
      ) : null}
      {metrics ? (
        <div className="kpi-grid" aria-live="polite">
          <KpiCard label="Threats Mitigated" value={metrics.threatsMitigated.toLocaleString()} delta={metrics.threatDelta} tone="good" />
          <KpiCard label="Compliance Score" value={`${metrics.complianceScore}%`} delta={metrics.complianceDelta} tone="good" />
          <KpiCard label="Customer Deployments" value={metrics.deployments.toLocaleString()} delta={metrics.deploymentsDelta} />
          <KpiCard label="System Uptime" value={`${metrics.uptime}%`} delta={metrics.uptimeDelta} tone="good" />
        </div>
      ) : (
        <p>Loading metrics…</p>
      )}
    </section>
  );
}
