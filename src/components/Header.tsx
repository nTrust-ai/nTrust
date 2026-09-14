import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="site-header" role="banner">
      <div className="container header-inner">
        <Link to="/" className="logo" aria-label="nTrust.ai Home">
          nTrust.ai
        </Link>
        <nav className="main-nav" aria-label="Primary navigation">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/services">Services</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
