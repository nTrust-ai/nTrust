// ============================================================
// nTrust.ai Dashboard — Real-time Security Analytics Components
// Deliverable for: TASK-040E16 (Dashboard Analytics Visualization Components)
// Performance-conscious: memoized, dependency-free SVG (no chart lib).
// ============================================================
import React, { useMemo } from "react";

function formatMetric(value) {
  if (value == null) return "—";
  return new Intl.NumberFormat("en-US", { notation: value > 9999 ? "compact" : "standard" }).format(value);
}

export const MetricCard = React.memo(function MetricCard({ label, value, delta, status = "neutral" }) {
  const tone = { good: "var(--nt-success)", warn: "var(--nt-warning)", bad: "var(--nt-danger)", neutral: "var(--nt-accent)" }[status];
  return (
    <article className="card" style={{ borderLeft: `3px solid ${tone}` }}>
      <p className="card__body" style={{ margin: 0, color: "var(--nt-text-muted)", fontSize: "0.82rem", textTransform: "uppercase", letterSpacing: "0.06em" }}>
        {label}
      </p>
      <div className="stat__value" style={{ fontSize: "1.9rem", color: tone }}>{formatMetric(value)}</div>
      {delta != null && (
        <p className="card__meta" style={{ color: delta < 0 ? "var(--nt-success)" : "var(--nt-danger)" }}>
          {delta < 0 ? "▼" : "▲"} {Math.abs(delta)}% vs prior period
        </p>
      )}
    </article>
  );
});

export function MetricsGrid({ metrics = [] }) {
  return (
    <div className="grid grid--3" role="list" aria-label="Security metrics">
      {metrics.map((m) => (
        <MetricCard key={m.id ?? m.label} {...m} />
      ))}
    </div>
  );
}

// Lightweight SVG sparkline/trend — no third-party dependency.
export const RiskTrendChart = React.memo(function RiskTrendChart({ series = [], height = 160, label = "Risk trend" }) {
  const { path, area, points } = useMemo(() => {
    if (!series.length) return { path: "", area: "", points: [] };
    const w = 600;
    const h = height;
    const max = Math.max(...series);
    const min = Math.min(...series);
    const span = max - min || 1;
    const px = (i) => (i / (series.length - 1)) * w;
    const py = (v) => h - ((v - min) / span) * (h - 16) - 8;
    const pts = series.map((v, i) => [px(i), py(v)]);
    const line = pts.map(([x, y], i) => `${i === 0 ? "M" : "L"}${x.toFixed(1)},${y.toFixed(1)}`).join(" ");
    const areaPath = `${line} L${w},${h} L0,${h} Z`;
    return { path: line, area: areaPath, points: pts };
  }, [series, height]);

  return (
    <div role="img" aria-label={label} style={{ background: "var(--nt-surface)", border: "1px solid var(--nt-border)", borderRadius: "var(--nt-radius)", padding: "1rem" }}>
      <svg viewBox={`0 0 600 ${height}`} width="100%" height={height} preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <linearGradient id="riskGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="var(--nt-accent)" stopOpacity="0.35" />
            <stop offset="100%" stopColor="var(--nt-accent)" stopOpacity="0" />
          </linearGradient>
        </defs>
        {area && <path d={area} fill="url(#riskGrad)" />}
        {path && <path d={path} fill="none" stroke="var(--nt-accent)" strokeWidth="2.5" strokeLinecap="round" />}
        {points.map(([x, y], i) => (
          <circle key={i} cx={x} cy={y} r="2.5" fill="var(--nt-accent)" />
        ))}
      </svg>
    </div>
  );
});
