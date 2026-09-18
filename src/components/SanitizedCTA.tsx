import React from 'react';
import { sanitizeCopy, resolveCTA, applyComingSoon } from '../utils/cta_alignment';

interface SanitizedCTAProps {
  href: string;
  label: string;
  isReleased?: boolean;
  className?: string;
}

const SanitizedCTA: React.FC<SanitizedCTAProps> = ({ 
  href, 
  label, 
  isReleased = true, 
  className = '' 
}) => {
  const resolvedHref = resolveCTA(href);
  const sanitizedLabel = sanitizeCopy(applyComingSoon(label, isReleased));

  return (
    <a 
      href={resolvedHref} 
      className={`cta-button ${className}`}
      aria-label={sanitizedLabel}
    >
      {sanitizedLabel}
    </a>
  );
};

export default SanitizedCTA;
