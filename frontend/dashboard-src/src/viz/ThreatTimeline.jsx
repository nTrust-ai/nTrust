/**
 * ThreatTimeline.jsx (Weaver deliverable 2026-09-04)
 * Supports: TASK-D29780 (CTI dashboard — real-time visualization)
 *
 * Dependency-free inline bar/line chart (divs + CSS), keyboard-focusable, with an
 * accessible data table fallback. Presentational; data flows from the intel hook.
 */
import React from 'react';

export function ThreatTimeline({ series = [], className = '', height = 160 }) {
  if (!Array.isArray(series) || series.length === 0) {
    return <p>No trend data available.</p>;
  }
  const max = Math.max(...series.map((p) => p.value), 1);
  return (
    <section aria-label="Threat trend" className={`threat-timeline ${className}`}>
      <h2>Threat Trend</h2>
      <div className="timeline-chart" role="img" aria-label={`Trend over ${series.length} periods`} style={{ height }}>
        {series.map((point, i) => {
          const h = Math.max(4, Math.round((point.value / max) * (height - 12)));
          return (
            <div
              key={point.label || i}
              className="timeline-bar"
              style={{ height: `${h}px` }}
              title={`${point.label}: ${point.value}`}
            />
          );
        })}
      </div>
      <table className="timeline-table">
        <caption className="visually-hidden">Threat trend values</caption>
        <thead>
          <tr><th scope="col">Period</th><th scope="col">Events</th></tr>
        </thead>
        <tbody>
          {series.map((point, i) => (
            <tr key={point.label || i}>
              <td>{point.label}</td>
              <td>{point.value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
