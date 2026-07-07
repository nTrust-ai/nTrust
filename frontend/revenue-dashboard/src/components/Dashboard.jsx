import React from 'react';
import { useTrustGuard } from '../hooks/useTrustGuard';
import { Shield, TrendingUp, AlertTriangle, CheckCircle } from 'lucide-react';

const Dashboard = () => {
  const { identityVerified, getThreatScore, getRecentThreats } = useTrustGuard();

  if (!identityVerified) {
    return (
      <div className="text-center py-12">
        <div className="bg-yellow-500/20 p-4 rounded-full w-16 h-16 mx-auto mb-4 flex items-center justify-center">
          <AlertTriangle className="w-8 h-8 text-yellow-500" />
        </div>
        <h2 className="text-2xl font-bold text-white mb-2">Authentication Required</h2>
        <p className="text-gray-400">Please complete the onboarding process to access your dashboard.</p>
      </div>
    );
  }

  const { score, level } = getThreatScore();
  const recentThreats = getRecentThreats(5);

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-white">Executive Dashboard</h1>
        <div className="flex items-center gap-2 bg-ntrust-surface px-4 py-2 rounded-lg border border-gray-700">
          <span className="text-sm text-gray-400">Security Status:</span>
          <span className={`font-semibold ${
            level === 'Low' ? 'text-green-500' : level === 'Medium' ? 'text-yellow-500' : 'text-red-500'
          }`}>
            {level} (Score: {score})
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-ntrust-surface rounded-xl p-6 border border-gray-700/50">
          <div className="flex items-center gap-3 mb-4">
            <Shield className="w-6 h-6 text-ntrust-primary" />
            <h3 className="text-lg font-semibold text-white">Overall Security Posture</h3>
          </div>
          <div className="text-4xl font-bold text-white mb-2">{score}%</div>
          <p className="text-sm text-gray-400">Real-time threat assessment score</p>
        </div>

        <div className="bg-ntrust-surface rounded-xl p-6 border border-gray-700/50">
          <div className="flex items-center gap-3 mb-4">
            <TrendingUp className="w-6 h-6 text-green-500" />
            <h3 className="text-lg font-semibold text-white">Threat Detection Rate</h3>
          </div>
          <div className="text-4xl font-bold text-white mb-2">99.8%</div>
          <p className="text-sm text-gray-400">Last 24 hours</p>
        </div>

        <div className="bg-ntrust-surface rounded-xl p-6 border border-gray-700/50">
          <div className="flex items-center gap-3 mb-4">
            <CheckCircle className="w-6 h-6 text-blue-500" />
            <h3 className="text-lg font-semibold text-white">Compliance Status</h3>
          </div>
          <div className="text-4xl font-bold text-white mb-2">Active</div>
          <p className="text-sm text-gray-400">All SLAs met</p>
        </div>
      </div>

      <div className="bg-ntrust-surface rounded-xl p-6 border border-gray-700/50">
        <h3 className="text-xl font-semibold text-white mb-4">Recent Threat Activity</h3>
        {recentThreats.length === 0 ? (
          <p className="text-gray-400 text-center py-8">No recent threats detected.</p>
        ) : (
          <div className="space-y-3">
            {recentThreats.map((threat) => (
              <div key={threat.id} className="flex items-center justify-between p-3 bg-ntrust-dark/50 rounded-lg border border-gray-700">
                <div className="flex items-center gap-3">
                  <AlertTriangle className={`w-5 h-5 ${
                    threat.severity === 'critical' ? 'text-red-500' :
                    threat.severity === 'high' ? 'text-orange-500' :
                    threat.severity === 'medium' ? 'text-yellow-500' : 'text-green-500'
                  }`} />
                  <div>
                    <p className="text-white font-medium capitalize">{threat.type}</p>
                    <p className="text-xs text-gray-400">Source: {threat.source}</p>
                  </div>
                </div>
                <div className="text-right">
                  <span className={`text-xs font-semibold ${
                    threat.severity === 'critical' ? 'text-red-500' :
                    threat.severity === 'high' ? 'text-orange-500' :
                    threat.severity === 'medium' ? 'text-yellow-500' : 'text-green-500'
                  }`}>
                    {threat.severity.toUpperCase()}
                  </span>
                  <p className="text-xs text-gray-400 mt-1">
                    {new Date(threat.timestamp).toLocaleTimeString()}
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Dashboard;