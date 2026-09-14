import React from 'react';
import { Link } from 'react-router-dom';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-900 text-white py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <div className="text-sm text-gray-400">
          &copy; {new Date().getFullYear()} nTrust.ai. All rights reserved.
        </div>
        <nav className="flex gap-6 text-sm">
          <Link to="/spine" className="hover:text-blue-400 transition-colors">
            Open Source (Spine Engine)
          </Link>
          <Link to="/contact" className="hover:text-blue-400 transition-colors">
            Contact Us
          </Link>
          <a href="https://github.com/ntrust-ai" target="_blank" rel="noopener noreferrer" className="hover:text-blue-400 transition-colors">
            GitHub
          </a>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;