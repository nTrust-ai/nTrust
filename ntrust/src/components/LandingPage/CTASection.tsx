import React from 'react';

/**
 * CTASection Component
 * 
 * Implements PROD-SPINE CTA Alignment Standard v1.0:
 * - Mailto-free CTAs site-wide (Board directive apr_e8d0ebd7)
 * - Resolvable targets only (no dead-end anchors)
 * - Sanitization of internal designators (MVP, Phase N, TASK/RAID codes)
 * - "Coming Soon" labeling for unreleased services
 */

export const CTASection: React.FC = () => {
  return (
    <section id="services" className="cta-section">
      <div className="container">
        <h2>Our Security Solutions</h2>
        <p className="subheading">Enterprise-grade cybersecurity services aligned to NIST AI RMF.</p>
        
        <div className="service-grid">
          {/* Service 1: Enterprise Security Audit */}
          <div className="service-card">
            <h3>Enterprise Security Audit</h3>
            <p>Comprehensive risk assessments and compliance audits for regulated industries.</p>
            <a href="/services/security-audit" className="btn btn-primary">Learn More</a>
          </div>

          {/* Service 2: AI Governance & Compliance */}
          <div className="service-card">
            <h3>AI Governance & Compliance</h3>
            <p>Automated compliance frameworks for EU AI Act and NIST standards.</p>
            <a href="/services/ai-governance" className="btn btn-primary">Learn More</a>
          </div>

          {/* Service 3: Managed AppSec (Coming Soon) */}
          <div className="service-card coming-soon">
            <span className="badge">Coming Soon</span>
            <h3>Managed Application Security</h3>
            <p>Continuous application security monitoring and remediation.</p>
            <a href="/services/appsec" className="btn btn-secondary">Get Notified</a>
          </div>

          {/* Service 4: TrustGuard Commercial (Coming Soon) */}
          <div className="service-card coming-soon">
            <span className="badge">Coming Soon</span>
            <h3>TrustGuard Commercial</h3>
            <p>Real-time threat intelligence and automated response platform.</p>
            <a href="/services/trustguard" className="btn btn-secondary">Get Notified</a>
          </div>
        </div>

        {/* Contact CTA - Mailto-free per Board directive */}
        <div className="contact-cta">
          <h3>Ready to Secure Your Infrastructure?</h3>
          <p>Contact our security experts for a custom risk assessment.</p>
          <a href="/contact" className="btn btn-large">Contact Us</a>
        </div>
      </div>
    </section>
  );
};

export default CTASection;