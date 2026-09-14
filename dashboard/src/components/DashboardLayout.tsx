/**
 * @file DashboardLayout.tsx
 * @description Primary shell for the nTrust.ai Dashboard MVP (PROD-BFBA88).
 *              Implements WCAG 2.2 AA compliant sidebar navigation and 
 *              responsive grid layout for TrustGuard metrics.
 */

import React from 'react';
import { Sidebar } from './Sidebar';
import { Header } from './Header';
import { MetricsGrid } from './MetricsGrid';
import { ThemeProvider } from '../context/ThemeContext';

export const DashboardLayout: React.FC = ({ children }) => {
  return (
    <ThemeProvider>
      <div className="flex h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
        {/* Sidebar Navigation */}
        <aside className="w-64 border-r border-gray-200 dark:border-gray-800 hidden md:block">
          <Sidebar />
        </aside>

        {/* Main Content Area */}
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Top Header with User Profile & Alerts */}
          <header className="h-16 border-b border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 px-6 flex items-center justify-between">
            <Header />
          </header>

          {/* Scrollable Dashboard Content */}
          <main className="flex-1 overflow-y-auto p-6">
            {children}
            
            {/* Default Dashboard Metrics View */}
            <div className="mt-4">
              <MetricsGrid />
            </div>
          </main>
        </div>
      </div>
    </ThemeProvider>
  );
};
