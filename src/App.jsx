import React, { useState } from 'react'

function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <div className="app">
       {/* Header */}
       <header>
         <div className="container">
           <nav className="nav">
             <a href="/" className="logo">nTrust<span>.ai</span></a>
             <div className={`nav-links ${mobileMenuOpen ? 'open' : ''}`}>
               <a onClick={() => window.location.href = '#features'}>Architecture</a>
               <a onClick={() => window.location.href = '#licensing'}>Licensing</a>
               <a onClick={() => window.location.href = '#roadmap'}>Roadmap</a>
               <button onClick={() => window.location.href = '/contact'} className="btn btn-primary">Enterprise Access</button>
             </div>
             <button className="mobile-toggle" onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
               {mobileMenuOpen ? '✕' : '☰'}
             </button>
           </nav>
         </div>
       </header>

       {/* Hero */}
       <section className="hero">
         <div className="container">
           <h1>Enterprise AI Security Infrastructure<br/>Deploying Now</h1>
           <p>We are engineering the next generation of zero-trust security and automated compliance. nTrust.ai delivers enterprise-grade threat intelligence, NIST AI RMF alignment, and proactive risk mitigation for modern organizations.</p>
           <div className="hero-ctas">
             <button onClick={() => window.location.href = '#licensing'} className="btn btn-primary">View Licensing Model</button>
             <button onClick={() => window.location.href = '/contact'} className="btn btn-outline">Request Enterprise Access</button>
           </div>
         </div>
       </section>

       {/* Architecture & Features */}
       <section id="features" className="features">
         <div className="container">
           <div className="section-header">
             <h2>Core Architecture</h2>
             <p>Built on a foundation of zero-trust principles, rigorous compliance frameworks, and scalable cloud-native infrastructure.</p>
           </div>
           <div className="grid">
             <div className="card">
               <div className="card-icon">🛡️</div>
               <h3>Zero-Trust Framework</h3>
               <p>All access requests are continuously verified. Micro-segmentation and least-privilege enforcement are baked into the core.</p>
             </div>
             <div className="card">
               <div className="card-icon">🔒</div>
               <h3>Automated Compliance</h3>
               <p>Built-in alignment with NIST AI RMF, SOC 2, and EU AI Act standards. Continuous audit logging ensures regulatory readiness.</p>
             </div>
             <div className="card">
               <div className="card-icon">🤖</div>
               <h3>AI-Driven Security</h3>
               <p>Predictive threat mapping and autonomous incident response. Designed to reduce MTTR and eliminate manual oversight gaps.</p>
             </div>
           </div>
         </div>
       </section>

       {/* Licensing Model */}
       <section id="licensing" className="licensing">
         <div className="container">
           <div className="section-header">
             <h2>Licensing Model</h2>
             <p>We offer strategic proprietary models. Source code availability is strictly governed by enterprise agreements.</p>
           </div>
           <div className="grid">
             <div className="service-card">
               <h3>Community Edition</h3>
               <span className="coming-soon">Free Tier Available</span>
               <ul className="service-features">
                 <li>Core Platform Access</li>
                 <li>Standard Security Modules</li>
                 <li>Community Support & Docs</li>
                 <li>Non-Production Use Allowed</li>
               </ul>
               <button onClick={() => window.location.href = '/contact'} className="btn btn-outline" style={{width: '100%', justifyContent: 'center'}}>Request Community Access</button>
             </div>
             <div className="service-card">
               <h3>Enterprise Edition</h3>
               <span className="coming-soon">NDA Required</span>
               <ul className="service-features">
                 <li>Full Source Code Access</li>
                 <li>Advanced AI & Compliance Suites</li>
                 <li>Dedicated Engineering Support</li>
                 <li>Custom Architecture & SLAs</li>
               </ul>
               <button onClick={() => window.location.href = '/contact'} className="btn btn-primary" style={{width: '100%', justifyContent: 'center'}}>Request NDA & Enterprise Access</button>
             </div>
           </div>
         </div>
       </section>

       {/* Roadmap */}
       <section id="roadmap" className="roadmap">
         <div className="container">
           <div className="section-header">
             <h2>Product Development Roadmap</h2>
             <p>Focused execution on Phase 1 delivery before expanding to subsequent product lines.</p>
           </div>
           <div className="timeline">
             <div className="phase">
               <h3>Phase 1: Core Platform (Current)</h3>
               <p>Zero-trust architecture, automated compliance mapping, and core security modules. Focus on stability, audit readiness, and enterprise access controls.</p>
             </div>
             <div className="phase">
               <h3>Phase 2: AI Threat Intelligence & SOC Integration</h3>
               <p>Predictive threat mapping, autonomous incident response, and 24/7 SOC monitoring integration. Enterprise-only rollout pending Phase 1 approval.</p>
             </div>
             <div className="phase">
               <h3>Phase 3: Profitability Scaling & Revenue Optimization</h3>
               <p>Commercial monetization, multi-tenant scaling, and strategic partnership integrations (ubaz inc.). Board-approved expansion phase.</p>
             </div>
           </div>
         </div>
       </section>

       {/* Contact / Enterprise Access */}
       <section id="contact" className="contact">
         <div className="container">
           <h2>Enterprise Access & NDA Request</h2>
           <p style={{color: 'var(--text-muted)', marginTop: '16px'}}>nTrust.ai is currently in active development. Enterprise customers requiring source code access must first execute a standard NDA. Community Edition access requests are processed on a rolling basis.</p>
           <form className="contact-form" onSubmit={(e) => { e.preventDefault(); alert('Request submitted successfully. We will contact you shortly.'); }}>
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
               <select required>
                 <option value="" disabled>Select Access Type</option>
                 <option value="community">Community Edition (Free)</option>
                 <option value="enterprise">Enterprise Edition (NDA Required)</option>
               </select>
             </div>
             <div className="form-group">
               <textarea rows="4" placeholder="How can we secure your organization?"></textarea>
             </div>
             <button type="submit" className="btn btn-primary" style={{width: '100%', justifyContent: 'center'}}>Submit Request</button>
           </form>
         </div>
       </section>

       {/* Footer */}
       <footer>
         <div className="container">
           <p>&copy; {new Date().getFullYear()} nTrust.ai — It's the numbers we trust. All rights reserved.</p>
           <p style={{marginTop: '8px', fontSize: '0.75rem'}}>Proprietary software. Source code is available under NDA for Enterprise customers only. Community Edition is free but not open source.</p>
         </div>
       </footer>
     </div>
   )
}

export default App
