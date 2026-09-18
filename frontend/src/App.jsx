import React, { useState } from 'react';
import './index.css';
import TrustGuardLanding from './pages/TrustGuardLanding';

const PRODUCTS = [
  {
    id: 'privacyguard',
    name: 'PrivacyGuard Suite',
    desc: 'Automated Privacy Compliance & Data Mapping. Enterprise-grade data governance tailored for modern regulatory landscapes.',
    status: 'active'
  },
  {
    id: 'trustaudit',
    name: 'TrustAudit Engine',
    desc: 'Continuous Vulnerability Scanning & Reporting. Proactive threat detection with automated remediation workflows.',
    status: 'active'
  },
  {
    id: 'ntrust-shield',
    name: 'nTrust Shield',
    desc: 'AI Incident Response Automation. Rapid containment and recovery powered by advanced machine learning models.',
    status: 'active'
  },
  {
    id: 'audit-service',
    name: 'Enterprise Security Audit Service',
    desc: 'NIST AI RMF Consulting & Implementation. Strategic gap assessments, remediation roadmaps, and full framework deployment.',
    status: 'active'
  },
  {
    id: 'trustguard',
    name: 'TrustGuard Platform',
    desc: 'Automated Cybersecurity & Compliance Pilot. 90-day monitored environments with SLA-backed assurance.',
    status: 'active',
    featured: true
  },
  {
    id: 'appsec-suite',
    name: 'Managed AppSec Services (ASPM & AppSOC)',
    desc: 'Consolidated Application Security Posture Management & SOC Operations. Continuous signal correlation and triage.',
    status: 'coming-soon'
  }
];

function App() {
  const [activeSection, setActiveSection] = useState('home');
  const [trustGuardActive, setTrustGuardActive] = useState(false);

  // Navigate to TrustGuard landing page
  const navigateToTrustGuard = () => {
    setTrustGuardActive(true);
    setActiveSection(null);
  };

  // Return to main app from TrustGuard
  const returnToHome = () => {
    setTrustGuardActive(false);
    setActiveSection('home');
  };

  if (trustGuardActive) {
    return <TrustGuardLanding onReturn={returnToHome} />;
  }

  return (
    <div className="app-container">
      <header className="header">
        <div className="container header-content">
          <div className="logo">nTrust.ai</div>
          <nav className="nav">
            <a href="#home" onClick={() => setActiveSection('home')}>Home</a>
            <a href="#services" onClick={() => setActiveSection('services')}>Services</a>
            <a href="#about" onClick={() => setActiveSection('about')}>About</a>
            <a href="#contact" className="btn btn-primary" onClick={() => setActiveSection('contact')}>Get Started</a>
          </nav>
        </div>
      </header>

      <main>
        {activeSection === 'home' && (
          <section id="home" className="hero">
            <div className="container hero-content">
              <h1>Enterprise AI Security & Compliance</h1>
              <p>Secure your infrastructure with zero-trust protocols, automated compliance workflows, and elite risk modeling. It's the numbers we trust.</p>
              <div className="hero-buttons">
                <a href="#services" className="btn btn-primary" onClick={() => setActiveSection('services')}>Explore Solutions</a>
                <a href="#contact" className="btn btn-secondary" onClick={() => setActiveSection('contact')}>Request Consultation</a>
              </div>
            </div>
          </section>
        )}

        {activeSection === 'services' && (
          <section id="services" className="services">
            <div className="container">
              <h2>Our Service Catalog</h2>
              <p className="section-subtitle">Comprehensive security solutions engineered for resilience and compliance.</p>
              <div className="product-grid">
                {PRODUCTS.map((prod) => (
                  <div key={prod.id} className={`product-card ${prod.featured ? 'featured' : ''}`}>
                    <div className="card-header">
                      <h3>{prod.name}</h3>
                      {prod.status === 'coming-soon' && <span className="badge badge-coming-soon">Coming Soon</span>}
                      {prod.featured && <span className="badge badge-featured">Featured</span>}
                    </div>
                    <p>{prod.desc}</p>
                    {prod.id === 'trustguard' ? (
                      <button className="btn btn-outline" onClick={navigateToTrustGuard}>View TrustGuard Pricing</button>
                    ) : (
                      <a href="#contact" className="btn btn-outline" onClick={() => setActiveSection('contact')}>Learn More</a>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        {activeSection === 'about' && (
          <section id="about" className="about">
            <div className="container">
              <h2>About nTrust.ai</h2>
              <p>nTrust.ai is a for-profit cybersecurity startup delivering cutting-edge AI-driven security architecture, risk modeling, and compliance automation. We partner with ubaz inc. to bring enterprise-grade protection to the North American market.</p>
              <div className="stats-grid">
                <div className="stat"><h4>99.9%</h4><p>SLA Uptime</p></div>
                <div className="stat"><h4>NIST AI RMF</h4><p>Compliant</p></div>
                <div className="stat"><h4>Zero-Trust</h4><p>Architecture</p></div>
              </div>
            </div>
          </section>
        )}

        {activeSection === 'contact' && (
          <section id="contact" className="contact">
            <div className="container contact-form-wrapper">
              <h2>Contact Us</h2>
              <p>Ready to secure your enterprise? Reach out to our team for a tailored security assessment.</p>
              <form className="contact-form" onSubmit={(e) => e.preventDefault()}>
                <input type="text" placeholder="Full Name" required />
                <input type="email" placeholder="Business Email" required />
                <select>
                  <option value="">Select Service Interest</option>
                  {PRODUCTS.map(p => <option key={p.id} value={p.id}>{p.name}</option>)}
                </select>
                <textarea placeholder="How can we help?" rows="5"></textarea>
                <button type="submit" className="btn btn-primary">Send Request</button>
              </form>
            </div>
          </section>
        )}
      </main>

      <footer className="footer">
        <div className="container">
          <p>&copy; {new Date().getFullYear()} nTrust.ai. All rights reserved.</p>
          <p>Partner: ubaz inc. | Privacy Policy | Terms of Service</p>
        </div>
      </footer>
    </div>
  );
}

export default App;