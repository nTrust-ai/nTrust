import React, { useState, useEffect } from 'react'

const App = () => {
  const [threatCount, setThreatCount] = useState(12)
  const [uptime, setUptime] = useState(99.97)
  const [complianceScore, setComplianceScore] = useState(98)
  const [auditLogs, setAuditLogs] = useState([])

  useEffect(() => {
    // Simulate real-time metrics updates
    const interval = setInterval(() => {
      setThreatCount(prev => Math.max(0, prev + Math.floor(Math.random() * 3) - 1))
      setUptime(prev => Number((prev + (Math.random() * 0.02 - 0.01)).toFixed(2)))
    }, 5000)

    // Generate initial audit logs
    const initialLogs = [
      { time: new Date().toISOString(), message: 'Dashboard initialized', status: 'INFO' },
      { time: new Date(Date.now() - 60000).toISOString(), message: 'Compliance check passed', status: 'SUCCESS' },
      { time: new Date(Date.now() - 120000).toISOString(), message: 'Threat scan completed: 3 blocked', status: 'SUCCESS' }
    ]
    setAuditLogs(initialLogs)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="app-container">
      <aside className="sidebar">
        <div className="logo">
          <ShieldIcon /> nTrust.ai
        </div>
        <nav>
          <div className="nav-item active">Dashboard</div>
          <div className="nav-item">Threats</div>
          <div className="nav-item">Compliance</div>
          <div className="nav-item">Audit Logs</div>
          <div className="nav-item">Settings</div>
        </nav>
      </aside>

      <main className="main-content">
        <header className="dashboard-header">
          <h1>Dashboard MVP</h1>
          <p style={{ color: 'var(--text-secondary)' }}>
            Enterprise Security Automation & Compliance Monitoring
          </p>
        </header>

        <section className="metrics-grid">
          <MetricCard 
            label="Active Threats" 
            value={threatCount} 
            trend="+2 this hour" 
            trendClass="trend-up" 
          />
          <MetricCard 
            label="System Uptime" 
            value={`${uptime}%`} 
            trend="SLA: 99.9%" 
            trendClass="trend-up" 
          />
          <MetricCard 
            label="Compliance Score" 
            value={`${complianceScore}%`} 
            trend="NIST/EU AI Act" 
            trendClass="trend-up" 
          />
        </section>

        <section className="audit-log-section">
          <h2>Recent Audit Events</h2>
          <div className="log-list">
            {auditLogs.map((log, index) => (
              <div key={index} className="log-item">
                <span className="log-time">{log.time.slice(0, 19).replace('T', ' ')}</span>
                <span>{log.message}</span>
                <span style={{ 
                  marginLeft: 'auto', 
                  padding: '0.25rem 0.5rem', 
                  borderRadius: '4px', 
                  fontSize: '0.75rem' 
                }}>
                  {log.status === 'INFO' && 'ℹ️'}
                  {log.status === 'SUCCESS' && '✅'}
                </span>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  )
}

const MetricCard = ({ label, value, trend, trendClass }) => (
  <div className="metric-card">
    <div className="metric-label">{label}</div>
    <div className="metric-value">{value}</div>
    <div className={`metric-trend ${trendClass}`}>{trend}</div>
  </div>
)

const ShieldIcon = () => (
  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
  </svg>
)

export default App