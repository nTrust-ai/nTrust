/**
 * main.jsx — Dashboard UI preview entry (Weaver deliverable 2026-09-04)
 * Composes the layout shell + widgets for empirical build verification.
 * Sanitized copy only. Not a production mount point; app wiring owned by Atlas.
 */
import React from 'react';
import { createRoot } from 'react-dom/client';
import { DashboardLayout } from './layout';
import { SunTokenPanel } from './widgets';
import { ExecutiveReport } from './widgets';
import { apiClient } from './api/apiClient';
import './widgets/widgets.css';

const DEMO_METRICS = [
  { key: 'revenue', label: 'Revenue (net)', value: 0, delta: 0, format: 'currency' },
  { key: 'margin', label: 'Gross margin', value: 0, delta: 0, format: 'percent' },
  { key: 'pipeline', label: 'Qualified pipeline', value: 0, delta: 0, format: 'currency' },
  { key: 'conversion', label: 'Pilot conversion', value: 0, delta: 0, format: 'percent' },
];

function Preview() {
  // Demonstrates that the API layer is importable and typed (shape-validated).
  const catalogAvailable = typeof apiClient.getCatalogProducts === 'function';

  return (
    <DashboardLayout
      brand="nTrust.ai"
      activeKey="overview"
      user={{ name: 'Preview User', email: 'preview@ntrust.ai' }}
      sessionStatus="authenticated"
      footer={<span>nTrust.ai — Security &amp; Compliance Dashboard Preview</span>}
    >
      <h1>Security Operations Overview</h1>
      <p>
        Preview composition of dashboard modules. API layer ready: {String(catalogAvailable)}.
      </p>
      <ExecutiveReport metrics={DEMO_METRICS} generatedAt={new Date().toISOString()} />
      <SunTokenPanel />
    </DashboardLayout>
  );
}

createRoot(document.getElementById('root')).render(<Preview />);
