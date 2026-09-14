import React from 'react';
import { Link } from 'react-router-dom';

const OpenSource: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto text-center">
        <h1 className="text-4xl font-extrabold text-gray-900 mb-6">
          Open Source & Community
        </h1>
        <p className="text-lg text-gray-600 mb-8">
          Explore our open-source initiatives, contribution guidelines, and community resources. 
          We welcome collaboration and transparent development practices aligned with enterprise security standards.
        </p>
        <div className="flex justify-center gap-4">
          <a 
            href="https://github.com/ntrust-ai" 
            target="_blank" 
            rel="noopener noreferrer"
            className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            View on GitHub
          </a>
          <Link 
            to="/spine" 
            className="inline-flex items-center px-6 py-3 border border-gray-300 text-base font-medium rounded-md shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Explore Spine Engine
          </Link>
        </div>
      </div>
    </div>
  );
};

export default OpenSource;