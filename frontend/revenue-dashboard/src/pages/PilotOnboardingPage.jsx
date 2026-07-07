import React, { useState } from 'react';
import PilotOnboardingWizard from '../components/PilotOnboardingWizard';
import useTrustGuard from '../hooks/useTrustGuard';

const DashboardFeed = () => {
  const [threats] = useState([
    { id: 1, type: 'SSL/TLS', status: 'Secure', score: 98 },
    { id: 2, type: 'Identity', status: 'Verified', score: 95 },
    { id: 3, type: 'Network', status: 'Monitoring', score: 99 },
  ]);

  return (
    <div style={{ background: '#1a1f2c', padding: '20px', borderRadius: '8px', border: '1px solid #3b82f6' }}>
      <h3 style={{ color: '#e2e8f0', marginBottom: '15px' }}>Dynamic Intelligence Feed</h3>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
        {threats.map(t => (
          <div key={t.id} style={{ 
            background: t.status === 'Secure' || t.status === 'Verified' ? '#064e3b' : '#78350f', 
            padding: '15px', 
            borderRadius: '6px', 
            color: '#fff',
            textAlign: 'center',
            border: `2px solid ${t.status === 'Secure' || t.status === 'Verified' ? '#10b981' : '#f59e0b'}`
          }}>
            <strong>{t.type}</strong><br/>
            <span style={{ fontSize: '0.9em', opacity: 0.9 }}>{t.status} ({t.score}%)</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default function PilotOnboardingPage() {
  const { trustScore, isVerified } = useTrustGuard();
  
  return (
    <div style={{ minHeight: '100vh', background: '#0f172a', color: '#e2e8f0', fontFamily: 'system-ui' }}>
      <header style={{ 
        background: 'linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%)', 
        padding: '20px 40px', 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center',
        boxShadow: '0 4px 6px -1px rgba(0,0,0,0.3)'
      }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.8rem' }}>nTrust.ai Pilot Portal</h1>
          <p style={{ margin: '5px 0 0', opacity: 0.8, fontSize: '0.9rem' }}>Phase 2: Traction & Trust</p>
        </div>
        <span className={`badge ${isVerified ? 'verified' : 'pending'}`} style={{ 
          background: isVerified ? '#10b981' : '#f59e0b', 
          padding: '8px 16px', 
          borderRadius: '20px', 
          fontWeight: 'bold',
          color: '#fff'
        }}>
          TrustScore: {trustScore} | {isVerified ? 'Identity Verified' : 'Pending Verification'}
        </span>
      </header>

      <main style={{ padding: '40px', maxWidth: '1200px', margin: '0 auto', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '30px' }}>
        <div className="wizard-section" style={{ background: '#1e293b', padding: '25px', borderRadius: '10px', border: '1px solid #475569' }}>
          <h2 style={{ marginTop: 0, color: '#60a5fa' }}>Pilot Onboarding</h2>
          <p style={{ opacity: 0.7, marginBottom: '20px' }}>Complete identity verification and security assessment to join the trust network.</p>
          <PilotOnboardingWizard />
        </div>

        <div className="feed-section">
          <DashboardFeed />
          <div style={{ marginTop: '20px', background: '#1e293b', padding: '20px', borderRadius: '8px', border: '1px solid #475569' }}>
            <h3 style={{ color: '#60a5fa', margin: '0 0 10px' }}>Zero-Trust Architecture</h3>
            <p style={{ opacity: 0.8, fontSize: '0.9rem' }}>
              All endpoints are continuously validated via TrustGuard telemetry. 
              Access is granted dynamically based on real-time risk scoring and identity proofing.
            </p>
          </div>
        </div>
      </main>

      <footer style={{ textAlign: 'center', padding: '20px', opacity: 0.5, fontSize: '0.8rem' }}>
        © 2026 nTrust.ai | Phase 2 Pilot Build v1.0 | Secure by Design
      </footer>
    </div>
  );
}