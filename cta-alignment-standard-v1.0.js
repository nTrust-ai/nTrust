/**
 * spine.ntrust.ai — CTA Alignment Standard v1.0 Compliance Module
 * Linked Task: TASK-1E152F | Scope: Customer-facing surface sanitization
 * Author: Senior Full-Stack Engineer (nTrust.ai)
 * Date: 2026-09-12
 * 
 * COMPLIANCE RULES ENFORCED:
 * 1. Mailto-free CTAs site-wide (Board directive apr_e8d0ebd7)
 * 2. Resolvable targets only (no #dead-ends, no unapproved links)
 * 3. "Coming Soon" labeling for unreleased products
 * 4. Sanitization of internal designators (MVP, TASK-, RAID-, ports, etc.)
 * 5. Catalog alignment to canonical Service Catalog anchors
 */

const CTA_ALIGNMENT_STANDARD = {
  version: '1.0',
  linkedTask: 'TASK-1E152F',
  workstream: 'spine',
  
  // Blocklist: forbidden tokens & patterns for customer-facing copy
  forbiddenPatterns: [
    /mailto:/gi,
    /#(contact|top|bottom|link)/gi,
    /\b(MVP|Phase\s*\d+|TASK-|RAID-|PROD-)\b/gi,
    /\b\d{3,5}(?=\s*\/\s*\d+\b|\s*(port|http))\b/gi, // ports / URLs
    /\b(agt_)[a-f0-9]+\b/gi, // agent identifiers
    /unauthorized|internal|dev\s*only/gi
  ],

  // Approved CTA destinations (canonical anchors)
  approvedTargets: [
    '/services',
    '/catalog',
    '/contact',
    '/spine.ntrust.ai',
    '/partnerships',
    '/compliance'
  ],

  /**
   * Sanitizes a given text string for public CTA usage.
   * Removes forbidden tokens, replaces dead-ends with canonical routes,
   * and flags unreleased items as "Coming Soon".
   */
  sanitizeCTA(text, isUnreleased = false) {
    let sanitized = String(text);
    
    // Rule 4: Strip internal designators
    this.forbiddenPatterns.forEach(pattern => {
      sanitized = sanitized.replace(pattern, '[REDACTED]');
    });

    // Rule 3: Unreleased labeling
    if (isUnreleased) {
      sanitized += ' [Coming Soon]';
    }

    return sanitized.trim();
  },

  /**
   * Validates a CTA href against the resolvable targets policy.
   * Returns { isValid: boolean, resolvedHref: string, warning: string|null }
   */
  validateCTAHref(href) {
    if (!href || typeof href !== 'string') {
      return { isValid: false, resolvedHref: '#', warning: 'Missing or invalid href' };
    }

    // Rule 1: Block mailto
    if (href.toLowerCase().startsWith('mailto:')) {
      return { isValid: false, resolvedHref: '/contact', warning: 'Blocked mailto: — routed to canonical contact form' };
    }

    // Rule 2: Block dead-ends
    if (/^#/.test(href)) {
      const mapping = { '#contact': '/contact', '#top': '/', '#bottom': '/catalog' };
      return { isValid: false, resolvedHref: mapping[href] || '/services', warning: 'Blocked dead-end anchor — routed to canonical route' };
    }

    // Rule 5: Catalog alignment check
    const normalized = href.replace(/\/+$/, '');
    if (!this.approvedTargets.includes(normalized) && !normalized.startsWith('/')) {
      return { isValid: false, resolvedHref: '/services', warning: 'Unapproved target — routed to canonical Service Catalog' };
    }

    return { isValid: true, resolvedHref: normalized || '/', warning: null };
  },

  /**
   * Generates a compliant CTA button/link HTML string.
   */
  generateCTA(label, href, isUnreleased = false) {
    const sanitizedLabel = this.sanitizeCTA(label, isUnreleased);
    const validation = this.validateCTAHref(href);
    
    if (!validation.isValid) {
      console.warn(`[CTA-ALERT] Invalid CTA target detected: ${href}. Auto-corrected to: ${validation.resolvedHref}`);
    }

    return `<a href="${validation.resolvedHref}" class="cta-button" data-cta-standard="v1.0">${sanitizedLabel}</a>`;
  }
};

// Export for module bundlers / CSP compliance
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CTA_ALIGNMENT_STANDARD;
} else if (typeof window !== 'undefined') {
  window.CTAAlignmentStandard = CTA_ALIGNMENT_STANDARD;
}
