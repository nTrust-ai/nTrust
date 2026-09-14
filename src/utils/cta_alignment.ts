/**
 * CTA Alignment & Sanitization Utility (PROD-SPINE Standard v1.0)
 * - Strips mailto: anchors, replaces with canonical contact form
 * - Ensures all targets resolve to real routes (no # dead-ends)
 * - Labels unreleased services "Coming Soon"
 * - Sanitizes internal codes (MVP, Phase N, TASK-/RAID-, ports, revenue)
 */

export const sanitizeCopy = (text: string): string => {
  let sanitized = text;
  // Strip internal designators
  const internalPatterns = [
    /\bMVP\b/gi,
    /\bPhase\s*\d+\b/gi,
    /TASK-[A-F0-9]{6}/gi,
    /RAID-[A-F0-9]{6}/gi,
    /PROD-[A-F0-9]{4,8}/gi,
    /:\d{4,5}\b/g, // ports
    /\$[\d,.]+\s*[KMB]/gi, // revenue targets
  ];
  internalPatterns.forEach((pattern) => {
    sanitized = sanitized.replace(pattern, '');
  });
  return sanitized.trim();
};

export const resolveCTA = (href: string): string => {
  if (!href || href.startsWith('mailto:')) {
    return '/contact'; // Canonical contact form route
  }
  if (href.startsWith('#')) {
    return '/services'; // Fallback to catalog anchor
  }
  return href;
};

export const applyComingSoon = (label: string, isReleased: boolean): string => {
  return isReleased ? label : `${label} (Coming Soon)`;
};

export const validateCTA = async (href: string): Promise<boolean> => {
  const resolved = resolveCTA(href);
  try {
    const response = await fetch(resolved, { method: 'HEAD', mode: 'no-cors' });
    return response.ok || response.status === 200;
  } catch {
    return false;
  }
};
