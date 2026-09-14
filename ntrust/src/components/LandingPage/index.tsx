import React from 'react';
import { CTASection } from './CTASection';
import { HeroBanner } from './HeroBanner';
import { FeatureGrid } from './FeatureGrid';

/**
 * LandingPage Component
 * 
 * Implements:
 * - Sanitization of internal designators (MVP, Phase N, TASK/RAID codes)
 * - Resolvable targets only (no dead-end anchors)
 * - Alignment with canonical Service Catalog
 */

export const LandingPage: React.FC = () => {
  return (
    <main className="landing-page">
      {/* Hero Section - Sanitized Copy per PROD-SPINE Spec */}
      <HeroBanner 
        title="It's the Numbers We Trust"
        subtitle="Elite cybersecurity strategy and architectural hardening for the modern enterprise."
        primaryCTA="/services"
        secondaryCTA="/about"
      />

      {/* Features Section - No internal codes, resolvable anchors */}
      <FeatureGrid 
        features={[
          {
            title: "NIST-Based Risk Models",
            description: "Custom risk frameworks aligned to federal standards.",
            href: "/services/risk-models"
          },
          {
            title: "SUN-Token NFC Security",
            description: "Advanced physical access control for secure facilities.",
            href: "/services/nfc-security"
          },
          {
            title: "Automated Compliance",
            description: "Continuous monitoring and reporting for EU AI Act compliance.",
            href: "/services/compliance-automation"
          }
        ]}
      />

      {/* CTA Section - Enforced via PROD-SPINE Standard */}
      <CTASection />

      {/* Footer - Mailto-free per Board directive */}
      <footer className="site-footer">
        <div className="container">
          <p>&copy; 2026 nTrust.ai. All rights reserved.</p>
          <nav>
            <a href="/privacy">Privacy Policy</a>
            <a href="/terms">Terms of Service</a>
            <a href="/contact">Contact</a>
          </nav>
        </div>
      </footer>
    </main>
  );
};

export default LandingPage;