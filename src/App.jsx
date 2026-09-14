import React, { useState } from 'react'
import { Shield, Lock, Brain, Globe, CheckCircle, ArrowRight, Menu, X } from 'lucide-react'

function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <div className="app">
      {/* Header */}
      <header>
        <div className="container">
          <nav className="nav">
            <a href="#" className="logo" aria-label="nTrust.ai Home">nTrust<span>.ai</span></a>
            <div className={`nav-links ${mobileMenuOpen ? 'open' : ''}`}>
              <a href="#features" onClick={() => setMobileMenuOpen(false)}>Solutions</a>
              <a href="#services" onClick={() => setMobileMenuOpen(false)}>Services</a>
              <a href="#contact" onClick={() => setMobileMenuOpen(false)}>Contact</a>
              <a href="#contact" className="btn btn-primary" onClick={() => setMobileMenuOpen(false)}>Request Demo</a>
            </div>
            <button 
              className="mobile-toggle" 
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              aria-label={mobileMenuOpen ? "Close menu" : "Open menu"}
              aria-expanded={mobileMenuOpen}
            >
              {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section className="hero" aria-labelledby="hero-heading">
        <div className="container">
          <h1 id="hero-heading">Enterprise AI Security<br/>That Actually Works</h1>
          <p>Protect your organization with nTrust.ai's zero-trust architecture, automated compliance mapping, and proactive threat intelligence. Built for modern enterprises.</p>
          <div className="hero-ctas">
            <a href="#services" className="btn btn-primary">Explore Services <ArrowRight size={18} /></a>
            <a href="#contact" className="btn btn-outline">Contact Sales</a>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="features" aria-labelledby="features-heading">
        <div className="container">
          <div className="section-header">
            <h2 id="features-heading">Core Capabilities</h2>
            <p>Our platform delivers measurable security outcomes through AI-driven automation and rigorous compliance frameworks.</p>
          </div>
          <div className="grid">
            <div className="card">
              <div className="card-icon"><Shield /></div>
              <h3>NIST Risk Modeling</h3>
              <p>Automated alignment with NIST AI RMF and SOC 2 frameworks. Continuous compliance monitoring with real-time audit trails.</p>
              <a href="#services" className="btn btn-outline">View Details</a>
            </div>
            <div className="card">
              <div className="card-icon"><Lock /></div>
              <h3>Zero-Trust Architecture</h3>
              <p>Enterprise-grade identity verification, micro-segmentation, and continuous access evaluation across all endpoints.</p>
              <a href="#services" className="btn btn-outline">View Details</a>
            </div>
            <div className="card">
              <div className="card-icon"><Brain /></div>
              <h3>AI Threat Intelligence</h3>
              <p>Predictive threat mapping and automated incident response. Reduce mean-time-to-respond by up to 70%.</p>
              <span className="coming-soon">Coming Soon</span>
            </div>
          </div>
        </div>
      </section>

      {/* Services */}
      <section id="services" className="services" aria-labelledby="services-heading">
        <div className="container">
          <div className="section-header">
            <h2 id="services-heading">Service Tiers</h2>
            <p>Scalable security solutions designed for your organization's growth stage.</p>
          </div>
          <div className="grid">
            <div className="service-card">
              <h3>Starter</h3>
              <div className="price">$4,999<span>/month</span></div>
              <ul className="service-features">
                <li>NIST Alignment Framework</li>
                <li>Basic Threat Monitoring</li>
                <li>Email Support</li>
                <li>Monthly Compliance Reports</li>
              </ul>
              <a href="#contact" className="btn btn-outline" style={{width: '100%', justifyContent: 'center'}}>Get Started</a>
            </div>
            <div className="service-card">
              <h3>Professional</h3>
              <div className="price">$14,999<span>/month</span></div>
              <ul className="service-features">
                <li>Advanced Risk Modeling</li>
                <li>24/7 SOC Monitoring</li>
                <li>Dedicated Security Analyst</li>
                <li>Automated Audit Logging</li>
                <li>API Integration Support</li>
              </ul>
              <a href="#contact" className="btn btn-primary" style={{width: '100%', justifyContent: 'center'}}>Contact Sales</a>
            </div>
            <div className="service-card">
              <h3>Enterprise</h3>
              <div className="price">$34,999<span>/month</span></div>
              <ul className="service-features">
                <li>Custom Architecture Design</li>
                <li>On-Premise Deployment</li>
                <li>Executive Dashboard</li>
                <li>Quarterly Penetration Testing</li>
                <li>SLA Guaranteed Uptime</li>
              </ul>
              <a href="#contact" className="btn btn-outline" style={{width: '100%', justifyContent: 'center'}}>Contact Sales</a>
            </div>
          </div>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="contact" aria-labelledby="contact-heading">
        <div className="container">
          <h2 id="contact-heading">Ready to Secure Your Enterprise?</h2>
          <p style={{color: 'var(--text-muted)', marginTop: '16px'}}>Our team will respond within 24 hours to schedule your personalized security assessment.</p>
          <form className="contact-form" onSubmit={(e) => e.preventDefault()}>
            <div className="form-group">
              <input type="text" placeholder="Full Name" required />
            </div>
            <div className="form-group">
              <input type="email" placeholder="Work Email" required />
            </div>
            <div className="form-group">
              <input type="text" placeholder="Company Name" required />
            </div>
            <div className="form-group">
              <textarea rows="4" placeholder="How can we help secure your organization?"></textarea>
            </div>
            <button type="submit" className="btn btn-primary" style={{width: '100%', justifyContent: 'center'}}>Submit Request</button>
          </form>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <div className="container">
          <p>&copy; {new Date().getFullYear()} nTrust.ai — It's the numbers we trust. All rights reserved.</p>
          <p style={{marginTop: '8px', fontSize: '0.75rem'}}>Enterprise AI Security & Compliance Automation</p>
        </div>
      </footer>
    </div>
  )
}

export default App
