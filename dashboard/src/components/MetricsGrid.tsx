/**
 * @file MetricsGrid.tsx
 * @description High-level metrics display for the nTrust.ai Dashboard.
 *              Designed to showcase TrustGuard compliance scores and 
 *              Website traffic/conversion data at a glance.
 */

import React from 'react';
import { Card } from './ui/Card';
import { TrendingUp, ShieldCheck, AlertCircle } from 'lucide-react'; // Assuming lucide-react for icons

interface MetricCardProps {
  title: string;
  value: string;
  trend?: string;
  icon: React.ReactNode;
  status?: 'success' | 'warning' | 'error';
}

const MetricCard: React.FC<MetricCardProps> = ({ title, value, trend, icon, status = 'success' }) => {
  const statusColors = {
    success: 'text-emerald-600 dark:text-emerald-400',
    warning: 'text-amber-600 dark:text-amber-400',
    error: 'text-red-600 dark:text-red-400',
  };

  return (
    <Card className="p-6 flex items-start justify-between hover:shadow-md transition-shadow">
      <div>
        <p className="text-sm font-medium text-gray-500 dark:text-gray-400">{title}</p>
        <h3 className="text-2xl font-bold mt-1">{value}</h3>
        {trend && (
          <span className={`text-xs font-medium ${statusColors[status]} flex items-center gap-1 mt-1`}>
            <TrendingUp className="w-3 h-3" /> {trend}
          </span>
        )}
      </div>
      <div className={`p-2 rounded-full bg-gray-100 dark:bg-gray-800 ${statusColors[status]}`}>
        {icon}
      </div>
    </Card>
  );
};

export const MetricsGrid: React.FC = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {/* Active Threats Neutralized */}
      <MetricCard 
        title="Active Threats Neutralized" 
        value="1,248" 
        trend="+12% from last week" 
        icon={<ShieldCheck className="w-5 h-5" />} 
        status="success"
      />
      
      {/* Compliance Score */}
      <MetricCard 
        title="TrustGuard Compliance" 
        value="98.4%" 
        trend="+2.1% improvement" 
        icon={<ShieldCheck className="w-5 h-5" />} 
        status="success"
      />

      {/* Critical Alerts */}
      <MetricCard 
        title="Critical Alerts" 
        value="3" 
        trend="-50% from last week" 
        icon={<AlertCircle className="w-5 h-5" />} 
        status="warning"
      />

      {/* Website Traffic (Cross-product data) */}
      <MetricCard 
        title="Website Visitors" 
        value="14.2k" 
        trend="+8% this month" 
        icon={<TrendingUp className="w-5 h-5" />} 
        status="success"
      />
    </div>
  );
};
