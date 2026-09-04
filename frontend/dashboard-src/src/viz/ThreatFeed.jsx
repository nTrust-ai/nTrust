/**
 * ThreatFeed.jsx (Weaver deliverable 2026-09-04)
 * Supports: TASK-D29780 (CTI Dashboard — real-time visualization), TASK-109D69 (threat intel integration)
 *
 * Live, accessible event feed with severity tone, timestamp and auto-remediation status.
 * Data is passed in from the intel hook; component stays presentational.
 */
import React from 'react';

const SEVERITY_TONE = {
  critical: 'red',
  high: 'orange',
  medium: 'yellow',
  low: 'blue',
  info: 'neutral',
};

export function ThreatFeed({ events = [], className = '', ariaLabel = 'Security operations feed' }) {
  return (
    <section aria-label={ariaLabel} className={`threat-feed ${className}`}>
      <h2>Security Operations Feed</h2>
      {events.length === 0 ? (
        <p>No recent events.</p>
      ) : (
        <ul className="feed-list">
          {events.map((event) => {
            const tone = SEVERITY_TONE[event.severity] || 'neutral';
            return (
              <li key={event.id} className={`feed-item tone-${tone}`}>
                <span className="feed-dot" aria-hidden="true" />
                <div className="feed-body">
                  <p className="feed-title">{event.title}</p>
                  <p className="feed-meta">
                    {event.statusLabel || (event.remediated ? 'Auto-remediated' : 'Open')} · {event.relativeTime}
                  </p>
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );
}
