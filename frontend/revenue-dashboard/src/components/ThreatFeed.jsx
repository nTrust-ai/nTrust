import React from 'react';
import { useTrustGuard } from '../hooks/useTrustGuard';
import { AlertTriangle, Shield, RefreshCw } from 'lucide-react';

const ThreatFeed = () => {
  const { getRecentThreats, clearTelemetry, identityVerified } = useTrustGuard();

  if (!identityVerified) {
    return (
      <div className="text-center py-12">
        <div className="bg-yellow-500/20 p-4 rounded-full w-16 h-16 mx-auto mb-4 flex items-center justify-center">
          <Shield className="w-8 h-8 text-yellow-500" />
        </div>
        <h2 className="text-2xl font-bold text-white mb-2">Access Denied</h2>
        <p className="text-gray-400">Complete onboarding to view the threat feed.</p>
      </div>
    );
  }

  const threats = getRecentThreats(50);

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-white">Live Threat Intelligence Feed</h1>
          <p className="text-gray-400 mt-1">Real-time monitoring of global cyber threats</p>
        </div>
        <button
          onClick={clearTelemetry}
          className="flex items-center gap-2 bg-ntrust-surface hover:bg-gray-700 px-4 py-2 rounded-lg border border-gray-700 transition-colors"
        >
          <RefreshCw className="w-4 h-4" />
          <span className="text-sm">Clear Feed</span>
        </button>
      </div>

      <div className="bg-ntrust-surface rounded-xl border border-gray-700/50 overflow-hidden">
        <div className="grid grid-cols-12 gap-4 p-4 bg-ntrust-dark/50 border-b border-gray-700 text-sm font-medium text-gray-400">
          <div className="col-span-2">Severity</div>
          <div className="col-span-3">Threat Type</div>
          <div className="col-span-2">Source</div>
          <div className="col-span-3">Timestamp</div>
          <div className="col-span-2">Status</div>
        </div>
        
        {threats.length === 0 ? (
          <div className="p-8 text-center text-gray-400">
            <Shield className="w-12 h-12 mx-auto mb-4 text-gray-600" />
            <p>No threats detected in the current session.</p>
          </div>
        ) : (
          <div className="divide-y divide-gray-700">
            {threats.map((threat) => (
              <div key={threat.id} className="grid grid-cols-12 gap-4 p-4 hover:bg-ntrust-dark/30 transition-colors">
                <div className="col-span-2">
                  <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-semibold ${
                    threat.severity === 'critical' ? 'bg-red-500/20 text-red-500' :
                    threat.severity === 'high' ? 'bg-orange-500/20 text-orange-500' :
                    threat.severity === 'medium' ? 'bg-yellow-500/20 text-yellow-500' :
                    'bg-green-500/20 text-green-500'
                  }`}>
                    {threat.severity.toUpperCase()}
                  </span>
                </div>
                <div className="col-span-3 text-white capitalize">{threat.type}</div>
                <div className="col-span-2 text-gray-400 text-sm">{threat.source}</div>
                <div className="col-span-3 text-gray-400 text-sm">
                  {new Date(threat.timestamp).toLocaleString()}
                </div>
                <div className="col-span-2">
                  <span className="inline-flex items-center gap-1 text-xs text-blue-400">
                    <Shield className="w-3 h-3" />
                    {threat.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="bg-ntrust-surface rounded-xl p-6 border border-gray-700/50">
        <h3 className="text-lg font-semibold text-white mb-4">Threat Intelligence Summary</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="bg-ntrust-dark/50 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-red-500">{threats.filter(t => t.severity === 'critical').length}</div>
            <div className="text-xs text-gray-400 mt-1">Critical</div>
          </div>
          <div className="bg-ntrust-dark/50 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-orange-500">{threats.filter(t => t.severity === 'high').length}</div>
            <div className="text-xs text-gray-400 mt-1">High</div>
          </div>
          <div className="bg-ntrust-dark/50 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-yellow-500">{threats.filter(t => t.severity === 'medium').length}</div>
            <div className="text-xs text-gray-400 mt-1">Medium</div>
          </div>
          <div className="bg-ntrust-dark/50 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-green-500">{threats.filter(t => t.severity === 'low').length}</div>
            <div className="text-xs text-gray-400 mt-1">Low</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ThreatFeed;