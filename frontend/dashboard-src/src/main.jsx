/**
 * main.jsx — nTrust.ai Customer Dashboard entry (Weaver 2026-09-04)
 * Composes the delivered dashboard modules (api/, auth/, viz/, reporting/, sunToken/)
 * into a single zero-trust SPA. Sanitized copy: no internal codes or phases.
 */
import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from './auth';
import { DashboardApp } from './app/DashboardApp';
import './app/dashboard.css';

const container = document.getElementById('root');

createRoot(container).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <DashboardApp />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
