import React, { useState } from 'react';
import './PricingStyles.css';

const PRICING_TIERS = [
  {
    name: 'Core',
    price: '$49/mo',
    annualPrice: '$39/mo (annual)',
    target: 'Solo SecOps / Individual Developers',
    features: [
      'AI-powered security scanning engine',
      'NIST AI RMF-aligned posture reports',
      'Real-time email alerts',
      '10 assets/month monitoring',
      '100 API calls/month',
      '30-day data retention',
      'Community support access',
      'Basic compliance templates'
    ],
    cta: 'Start Free Trial',
    popular: true,
    status: 'active'
  },
  {
    name: 'Pro',
    price: '$199/mo',
    annualPrice: '$159/mo (annual)',
    target: 'SMB Teams / Growth Companies',
    features: [
      'Everything in Core',
      'Advanced compliance mapping (SOC2, GDPR, CCPA)',
      'Continuous security monitoring & AI analysis',
      'Automated remediation workflows',
      'Full API access for integrations',
      '50 assets/month monitoring',
      '1,000 API calls/month',
      '90-day data retention',
      'Priority email support',
      '99.5% uptime SLA',
      '<4hr response time'
    ],
    cta: 'Start Pro Trial',
    popular: false,
    status: 'active'
  },
  {
    name: 'Team',
    price: '$599/mo',
    annualPrice: '$499/mo (annual)',
    target: 'Mid-Market Organizations',
    features: [
      'Everything in Pro',
      'Multi-tenant RBAC architecture',
      'Executive compliance dashboards',
      '200 assets/month monitoring',
      '5,000 API calls/month',
      'Unlimited data retention (1-year minimum)',
      'SSO/RBAC integration support',
      'Custom policy enforcement engine',
      'Dedicated account manager',
      '99.9% uptime SLA',
      '<1hr response time'
    ],
    cta: 'Contact Sales',
    popular: false,
    status: 'active'
  },
  {
    name: 'Enterprise',
    price: 'Custom Pricing',
    annualPrice: 'Starting at $15K/year',
    target: 'Fortune 500 / Government Entities',
    features: [
      'Everything in Team',
      'Dedicated infrastructure deployment',
      'White-label platform options',
      'Unlimited assets & API calls',
      '24/7 CISO advisory services',
      'Custom integration development',
      'SUN-token NFC hardening module',
      'On-premise or hybrid deployment',
      '99.9% uptime SLA with penalty clauses',
      '<30min response time guarantee'
    ],
    cta: 'Request Enterprise Demo',
    popular: false,
    status: 'coming-soon'
  }
];

function TrustGuardLanding() {
  const [billingCycle, setBillingCycle] = useState('monthly');
  const [selectedTier, setSelectedTier] = useState(null);
  const [activeSection, setActiveSection] = useState('overview');

  return (
    <div className="trustguard-landing-page">
      {/* Hero Section */}
      <header className="trustguard-hero">
        <div className="container hero-content">
          <h1>TrustGuard MVP</h1>
          <p className="hero-subtitle">Automated Cybersecurity & Compliance Pilot — 90-Day Monitored Environments with SLA-Backed Assurance</p>
          <p className="hero-tagline"><em>"It is the numbers we trust."</em></p>
          
          <div className="hero-buttons">
            <button className="btn btn-primary" onClick={() => setActiveSection('pricing')}>View Pricing</button>
            <button className="btn btn-outline" onClick={() => setActiveSection('features')}>Explore Features</button>
            <button className="btn btn-secondary" onClick={() => window.location.href = '/contact'}>Request Consultation</button>
          </div>

          <div className="trust-badges">
            <span className="badge">✓ NIST AI RMF Compliant</span>
            <span className="badge">✓ EU AI Act Aligned</span>
            <span className="badge">✓ Zero-Trust Architecture</span>
            <span className="badge">✓ SOC2 Type II Ready</span>
          </div>
        </div>
      </header>

      {/* Overview Section */}
      {activeSection === 'overview' && (
        <section className="trustguard-overview">
          <div className="container">
            <h2>What is TrustGuard?</h2>
            <p>TrustGuard MVP is a cutting-edge cybersecurity platform that automates compliance validation through continuous security monitoring and AI-driven risk analysis. Designed for organizations that need to prove regulatory readiness without the overhead of manual audits.</p>
            
            <div className="value-props">
              <div className="prop-card">
                <h3>🤖 Automation-First</h3>
                <p>Reduce manual audit overhead by 60% through continuous monitoring and automated evidence collection.</p>
              </div>
              <div className="prop-card">
                <h3>🔒 Privacy-First</h3>
                <p>Zero-trust architecture with NIST AI RMF alignment ensures data sovereignty and compliance.</p>
              </div>
              <div className="prop-card">
                <h3>📊 Intelligence-Driven</h3>
                <p>Evidence-based security metrics that demonstrate compliance readiness in real-time.</p>
              </div>
            </div>

            <div className="metrics-grid">
              <div className="metric">
                <h4>99.5%+</h4>
                <p>SLA Uptime</p>
              </div>
              <div className="metric">
                <h4>&lt;4hr</h4>
                <p>Avg Response Time</p>
              </div>
              <div className="metric">
                <h4>60%</h4>
                <p>Audit Overhead Reduction</p>
              </div>
              <div className="metric">
                <h4>LTV:CAC 7.8:1</h4>
                <p>Customer Value Ratio</p>
              </div>
            </div>
          </div>
        </section>
      )}

      {/* Pricing Section */}
      {activeSection === 'pricing' && (
        <section className="trustguard-pricing-section">
          <div className="container">
            <h2>Tiered Pricing for Every Scale</h2>
            <p className="section-subtitle">Transparent, usage-based pricing designed to grow with your organization.</p>

            <div className="billing-toggle">
              <span className={billingCycle === 'monthly' ? 'active' : ''}>Monthly Billing</span>
              <button 
                className="toggle-switch" 
                onClick={() => setBillingCycle(billingCycle === 'monthly' ? 'annual' : 'monthly')}
              >
                <span className={billingCycle === 'annual' ? 'on' : 'off'}></span>
              </button>
              <span className={billingCycle === 'annual' ? 'active' : ''}>Annual Billing <span className="badge-save">Save 20%</span></span>
            </div>

            <div className="pricing-grid">
              {PRICING_TIERS.map((tier) => (
                <div key={tier.name} className={`pricing-card ${tier.popular ? 'popular' : ''} ${tier.status === 'coming-soon' ? 'disabled' : ''}`}>
                  {tier.popular && <div className="popular-badge">Best Value</div>}
                  
                  <div className="card-header">
                    <h2>{tier.name}</h2>
                    {tier.status === 'coming-soon' && <span className="badge-coming-soon">Coming Soon</span>}
                  </div>

                  <div className="pricing">
                    <div className="price">{billingCycle === 'annual' && tier.annualPrice ? tier.annualPrice : tier.price}</div>
                    {billingCycle === 'annual' && !tier.annualPrice && <div className="price">{tier.price}</div>}
                    {billingCycle === 'monthly' && tier.annualPrice && (
                      <div className="annual-price">Or {tier.annualPrice}</div>
                    )}
                  </div>

                  <p className="target-segment">{tier.target}</p>

                  <ul className="feature-list">
                    {tier.features.map((feature, idx) => (
                      <li key={idx}>✓ {feature}</li>
                    ))}
                  </ul>

                  <button 
                    className={`btn ${tier.popular ? 'btn-primary' : 'btn-outline'}`}
                    onClick={() => setSelectedTier(tier.name)}
                    disabled={tier.status === 'coming-soon'}
                  >
                    {tier.cta}
                  </button>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Enterprise SOW */}
      <section className="trustguard-enterprise">
        <div className="container">
          <h2>Enterprise SOW Options</h2>
          <p className="section-subtitle">Custom engagements for mission-critical deployments.</p>
          
          <div className="sow-options">
            <div className="sow-card">
              <h3>Assess</h3>
              <div className="price">$15,000</div>
              <ul>
                <li>Comprehensive gap assessment & risk analysis</li>
                <li>NIST AI RMF alignment review</li>
                <li>Detailed remediation roadmap</li>
                <li>Executive briefing deck</li>
              </ul>
            </div>
            <div className="sow-card">
              <h3>Harden</h3>
              <div className="price">$35,000</div>
              <ul>
                <li>Full framework deployment & configuration</li>
                <li>Automated compliance workflow implementation</li>
                <li>Staff training & enablement program</li>
                <li>90-day post-deployment support</li>
              </ul>
            </div>
            <div className="sow-card">
              <h3>Managed Resilience</h3>
              <div className="price">$50,000</div>
              <ul>
                <li>Dedicated infrastructure & white-label platform</li>
                <li>24/7 monitoring & incident response</li>
                <li>Continuous optimization & quarterly reviews</li>
                <li>Unlimited support & advisory access</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Partnership */}
      <section className="trustguard-partnership">
        <div className="container">
          <h3>🤝 Strategic Partnership: ubaz inc.</h3>
          <p>TrustGuard MVP is available through our exclusive partnership with ubaz inc. White-label API access and reseller programs are available for qualified partners. Contact sales for margin structure (20% tiered, 15% enterprise).</p>
        </div>
      </section>

      {/* FAQ */}
      <section className="trustguard-faq">
        <div className="container">
          <h2>Frequently Asked Questions</h2>
          
          <div className="faq-item">
            <h3>What makes TrustGuard different from traditional security tools?</h3>
            <p>TrustGuard combines AI-powered automated scanning with continuous compliance validation, providing real-time evidence of regulatory readiness without manual audit overhead.</p>
          </div>
          
          <div className="faq-item">
            <h3>Can I upgrade or downgrade my tier at any time?</h3>
            <p>Yes! All tiers can be upgraded or downgraded with immediate effect. Prorated billing applies for mid-cycle changes.</p>
          </div>
          
          <div className="faq-item">
            <h3>What compliance frameworks do you support?</h3>
            <p>We natively support SOC2 Type II, NIST AI RMF, GDPR, CCPA, and HIPAA readiness assessments. Custom framework mappings available for Enterprise tier.</p>
          </div>
          
          <div className="faq-item">
            <h3>Is there a free trial available?</h3>
            <p>Yes! All tiers include a 14-day free trial with full feature access. No credit card required to start.</p>
          </div>
        </div>
      </section>

      {/* Compliance Badges */}
      <section className="trustguard-compliance">
        <div className="container">
          <div className="compliance-badges">
            <span className="badge">✓ NIST AI RMF Compliant</span>
            <span className="badge">✓ EU AI Act Aligned</span>
            <span className="badge">✓ Zero-Trust Architecture</span>
            <span className="badge">✓ SOC2 Type II Ready</span>
            <span className="badge">✓ AES-256 Encryption</span>
            <span className="badge">✓ TLS 1.3 Enforcement</span>
          </div>
        </div>
      </section>

      {/* CTA Footer */}
      <footer className="trustguard-footer">
        <div className="container">
          <h2>Ready to prove compliance readiness?</h2>
          <p>Start your TrustGuard MVP trial today — no credit card required.</p>
          <button className="btn btn-primary" style={{width: 'auto'}}>Get Started Free</button>
        </div>
      </footer>

      {/* Selection Modal */}
      {selectedTier && (
        <div className="selection-modal" onClick={() => setSelectedTier(null)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h3>You selected: {selectedTier}</h3>
            <p>Redirecting to billing integration... <br/><em>(Stripe/Plaid setup required for full activation)</em></p>
            <button className="btn btn-primary" onClick={() => setSelectedTier(null)}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default TrustGuardLanding;