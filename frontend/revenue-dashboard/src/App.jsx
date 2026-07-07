import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { TrustGuardProvider } from './hooks/useTrustGuard';
import PilotOnboardingWizard from './components/PilotOnboardingWizard';
import Dashboard from './components/Dashboard';
import ThreatFeed from './components/ThreatFeed';
import './index.css';

function App() {
  return (
    <TrustGuardProvider>
      <Router>
        <div className="min-h-screen bg-ntrust-dark text-white">
          <nav className="bg-ntrust-surface border-b border-gray-700/50 px-6 py-4">
            <div className="max-w-7xl mx-auto flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="bg-ntrust-primary p-2 rounded-lg">
                  <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                  </svg>
                </div>
                <div>
                  <h1 className="text-xl font-bold text-white">nTrust.ai</h1>
                  <p className="text-xs text-gray-400">It is the numbers we trust</p>
                </div>
              </div>
              <div className="flex items-center gap-4">
                <span className="text-sm text-gray-400">Phase 2: Traction & Trust</span>
                <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              </div>
            </div>
          </nav>

          <main className="max-w-7xl mx-auto px-6 py-8">
            <Routes>
              <Route path="/" element={<Navigate to="/onboarding" replace />} />
              <Route path="/onboarding" element={<PilotOnboardingWizard />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/threats" element={<ThreatFeed />} />
            </Routes>
          </main>

          <footer className="border-t border-gray-700/50 px-6 py-4 mt-auto">
            <div className="max-w-7xl mx-auto text-center text-sm text-gray-400">
              &copy; 2026 nTrust.ai | Cybersecurity & Privacy Solutions | v2.0.0
            </div>
          </footer>
        </div>
      </Router>
    </TrustGuardProvider>
  );
}

export default App;