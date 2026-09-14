import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="site-footer" role="contentinfo">
      <div className="container footer-inner">
        <p>&copy; {new Date().getFullYear()} nTrust.ai. All rights reserved.</p>
        <nav aria-label="Footer navigation">
          <a href="/privacy">Privacy Policy</a>
          <a href="/terms">Terms of Service</a>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;
