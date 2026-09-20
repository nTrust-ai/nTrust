import React, { useState } from 'react';
import { Shield, Activity, Lock, CheckCircle, AlertTriangle, Server, BarChart3, Zap } from 'lucide-react';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');

  return (
     <div style={{ fontFamily: 'system-ui, -apple-system, sans-serif', backgroundColor: '#0f172a', minHeight: '100vh', color: '#e2e8f0' }}>
       <header style={{ backgroundColor: '#1e293b', padding: '1rem 2rem', borderBottom: '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
         <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
           <Shield size={32} color="#38bdf8" />
           <h1 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 700 }}>TrustGuard AI</h1>
         </div>
         <nav style={{ display: 'flex', gap: '1rem' }}>
           {['dashboard', 'compliance', 'risks', 'settings'].map(tab => (
             <button key={tab} onClick={() => setActiveTab(tab)} style={{ background: activeTab === tab ? '#3b82f6' : 'transparent', color: '#fff', border: 'none', padding: '0.5rem 1rem', borderRadius: '0.375rem', cursor: 'pointer', fontWeight: 500 }}>
               {tab.charAt(0).toUpperCase() + tab.slice(1)}
             </button>
           ))}
         </nav>
       </header>

       <main style={{ padding: '2rem' }}>
         <div style={{ marginBottom: '2rem' }}>
           <h2 style={{ margin: 0, fontSize: '1.875rem', fontWeight: 600 }}>Compliance Dashboard</h2>
           <p style={{ color: '#94a3b8', marginTop: '0.5rem' }}>Real-time NIST AI RMF & EU AI Act Monitoring</p>
         </div>

         <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
           {[
             { icon: Activity, label: 'System Uptime', value: '99.98%', color: '#10b981' },
             { icon: Lock, label: 'Threat Level', value: 'Low', color: '#3b82f6' },
             { icon: CheckCircle, label: 'Compliance Score', value: '94/100', color: '#8b5cf6' },
             { icon: AlertTriangle, label: 'Active Risks', value: '2', color: '#f59e0b' }
           ].map((stat, i) => (
             <div key={i} style={{ backgroundColor: '#1e293b', padding: '1.5rem', borderRadius: '0.75rem', border: '1px solid #334155' }}>
               <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                 <span style={{ color: '#94a3b8', fontSize: '0.875rem' }}>{stat.label}</span>
                 <stat.icon size={18} color={stat.color} />
               </div>
               <div style={{ fontSize: '1.5rem', fontWeight: 700, color: stat.color }}>{stat.value}</div>
             </div>
           ))}
         </div>

         <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))', gap: '1.5rem' }}>
           <div style={{ backgroundColor: '#1e293b', padding: '1.5rem', borderRadius: '0.75rem', border: '1px solid #334155' }}>
             <h3 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '0.5rem' }}><Server size={20} color="#38bdf8" /> Active Workflows</h3>
             <ul style={{ listStyle: 'none', padding: 0 }}>
               {['NIST AI Risk Assessment', 'EU AI Act Compliance Audit', 'Model Governance Check'].map((wf, i) => (
                 <li key={i} style={{ padding: '0.75rem 0', borderBottom: '1px solid #334155', display: 'flex', justifyContent: 'space-between' }}>
                   <span>{wf}</span>
                   <span style={{ color: '#10b981', fontSize: '0.875rem' }}>Active</span>
                 </li>
               ))}
             </ul>
           </div>

           <div style={{ backgroundColor: '#1e293b', padding: '1.5rem', borderRadius: '0.75rem', border: '1px solid #334155' }}>
             <h3 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '0.5rem' }}><BarChart3 size={20} color="#8b5cf6" /> Risk Mitigation</h3>
             <div style={{ height: '150px', backgroundColor: '#0f172a', borderRadius: '0.5rem', display: 'flex', alignItems: 'center', justifyContent: 'center', border: '1px dashed #334155' }}>
               <span style={{ color: '#64748b' }}>Live Risk Analytics Feed</span>
             </div>
           </div>
         </div>

         <footer style={{ marginTop: '2rem', textAlign: 'center', color: '#64748b', fontSize: '0.875rem' }}>
          TrustGuard AI © 2026 nTrust.ai | Enterprise-Grade Cybersecurity & Compliance Platform
         </footer>
       </main>
     </div>
   );
};

export default App;
