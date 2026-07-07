import { createContext, useContext, useState, useEffect } from 'react';

const TrustGuardContext = createContext(null);

export const useTrustGuard = () => {
  const context = useContext(TrustGuardContext);
  if (!context) {
    throw new Error('useTrustGuard must be used within a TrustGuardProvider');
  }
  return context;
};

export const TrustGuardProvider = ({ children }) => {
  const [identityVerified, setIdentityVerified] = useState(false);
  const [threatScore, setThreatScore] = useState(0);
  const [telemetry, setTelemetry] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  // Simulate real-time threat feed
  useEffect(() => {
    if (identityVerified) {
      const interval = setInterval(() => {
        const newThreat = {
          id: Date.now(),
          type: ['phishing', 'malware', 'ddos', 'unauthorized_access'][Math.floor(Math.random() * 4)],
          severity: ['low', 'medium', 'high', 'critical'][Math.floor(Math.random() * 4)],
          source: `IP-${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}`,
          timestamp: new Date().toISOString(),
          status: 'detected'
        };
        setTelemetry(prev => [newThreat, ...prev].slice(0, 50));
        setThreatScore(prev => Math.min(prev + Math.random() * 5, 100));
      }, 5000);

      return () => clearInterval(interval);
    }
  }, [identityVerified]);

  const verifyIdentity = async (companyName) => {
    setIsLoading(true);
    // Simulate API call to identity verification service
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Mock verification logic
    const isValid = companyName.length > 2 && !isNaN(Math.random());
    
    if (isValid) {
      setIdentityVerified(true);
      setThreatScore(Math.random() * 30); // Initial low threat score
    }
    
    setIsLoading(false);
    return { success: isValid, message: isValid ? 'Identity verified' : 'Verification failed' };
  };

  const getThreatScore = () => {
    return {
      score: Math.round(threatScore),
      level: threatScore < 30 ? 'Low' : threatScore < 60 ? 'Medium' : 'High',
      trend: 'stable'
    };
  };

  const getRecentThreats = (limit = 10) => {
    return telemetry.slice(0, limit);
  };

  const clearTelemetry = () => {
    setTelemetry([]);
    setThreatScore(0);
  };

  return (
    <TrustGuardContext.Provider value={{
      identityVerified,
      threatScore,
      telemetry,
      isLoading,
      verifyIdentity,
      getThreatScore,
      getRecentThreats,
      clearTelemetry
    }}>
      {children}
    </TrustGuardContext.Provider>
  );
};

export default TrustGuardProvider;