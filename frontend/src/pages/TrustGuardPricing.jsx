import React, { useState } from 'react';

const PRICING_TIERS = [
  {
    name: 'Starter',
    price: '$49/mo',
    annualPrice: '$39/mo (annual)',
    target: 'Solo SecOps / Developers',
    features: [
      'Core scanning engine',
      'Basic security reports',
      'NIST-aligned posture reports',
      'Email alerts',
      '10 assets/month',
      '100 API calls/month',
      '30-day data retention',
      'Community support'
    ],
    cta: 'Start Free Trial',
    popular: false,
    status: 'active'
  },
  {
    name: 'Pro',
    price: '$199/mo',
    annualPrice: '$159/mo (annual)',
    target: 'SMB / Growth Teams',
    features: [
      'Everything in Starter',
      'Advanced NIST mapping (SOC2, GDPR, CCPA)',
      'Continuous security monitoring',
      'Automated remediation workflows',
      'Full API access',
      '50 assets/month',
      '1,000 API calls/month',
      '90-day data retention',
      'Priority email support',
      '99.5% uptime SLA',
      '<4hr response time'
    ],
    cta: 'Start Pro Trial',
    popular: true,
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
      'Compliance dashboards & reporting',
      '200 assets/month',
      '5,000 API calls/month',
      'Unlimited data retention (1-year min)',
      'SSO/RBAC integration',
      'Custom policy enforcement',
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
    target: 'Fortune 500 / Government',
    features: [
      'Everything in Team',
      'Dedicated infrastructure',
      'White-label options',
      'Unlimited assets & API calls',
      '24/7 CISO advisory',
      'Custom integrations',
      'SUN-token NFC hardening',
      'On-premise deployment option',
      '99.9% uptime SLA',
      '<30min response time'
    ],
    cta: 'Request Enterprise Demo',
    popular: false,
    status: 'coming-soon'
  }
];

function TrustGuardPricing() {
  const [billingCycle, setBillingCycle] = useState('monthly');
  const [selectedTier, setSelectedTier] = useState(null);

  return (
    <div className="trustguard-pricing-page">
      <header className="pricing-header">
        <h1>TrustGuard MVP — Pricing & Commercialization</h1>
        <p className="subtitle">Automated cybersecurity intelligence that proves compliance readiness. Tiered pricing for every scale.</p>
        
        <div className="billing-toggle">
          <span className={billingCycle === 'monthly' ? 'active' : ''}>Monthly</span>
          <button 
            className="toggle-switch" 
            onClick={() => setBillingCycle(billingCycle === 'monthly' ? 'annual' : 'monthly')}
          >
            <span className={billingCycle === 'annual' ? 'on' : 'off'}></span>
          </button>
          <span className={billingCycle === 'annual' ? 'active' : ''}>Annual <span className="badge-save">Save 20%</span></span>
        </div>
      </header>

      <section className="pricing-grid">
        {PRICING_TIERS.map((tier) => (
          <div key={tier.name} className={`pricing-card ${tier.popular ? 'popular' : ''} ${tier.status === 'coming-soon' ? 'disabled' : ''}`}>
            {tier.popular && <div className="popular-badge">Most Popular</div>}
            
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
      </section>

      <section className="enterprise-sow">
        <h2>Enterprise SOW Options</h2>
        <div className="sow-options">
          <div className="sow-card">
            <h3>Assess</h3>
            <div className="price">$15,000</div>
            <ul>
              <li>Gap assessment & risk analysis</li>
              <li>NIST AI RMF alignment review</li>
              <li>Remediation roadmap</li>
            </ul>
          </div>
          <div className="sow-card">
            <h3>Harden</h3>
            <div className="price">$35,000</div>
            <ul>
              <li>Full framework deployment</li>
              <li>Automated compliance workflows</li>
              <li>Staff training & enablement</li>
            </ul>
          </div>
          <div className="sow-card">
            <h3>Managed Resilience</h3>
            <div className="price">$50,000</div>
            <ul>
              <li>Dedicated infrastructure</li>
              <li>24/7 monitoring & support</li>
              <li>Continuous optimization</li>
            </ul>
          </div>
        </div>
      </section>

      <section className="partnership-note">
        <h3>🤝 ubaz inc. Partnership</h3>
        <p>White-label TrustGuard API available through our strategic partnership with ubaz inc. Contact sales for reseller margin structure (20% tiered, 15% enterprise).</p>
      </section>

      <section className="compliance-badges">
        <div className="badge">✓ NIST AI RMF Compliant</div>
        <div className="badge">✓ EU AI Act Aligned</div>
        <div className="badge">✓ Zero-Trust Architecture</div>
        <div className="badge">✓ SOC2 Type II Ready</div>
      </section>

      {selectedTier && (
        <div className="selection-modal" onClick={() => setSelectedTier(null)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h3>You selected: {selectedTier}</h3>
            <p>Redirecting to billing integration... (Stripe/Plaid setup required)</p>
            <button className="btn btn-primary" onClick={() => setSelectedTier(null)}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default TrustGuardPricing;