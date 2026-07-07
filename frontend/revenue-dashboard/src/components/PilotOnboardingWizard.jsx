import React, { useState } from 'react';
import { Shield, CheckCircle, AlertTriangle, Lock, ArrowRight, ChevronRight } from 'lucide-react';
import { useTrustGuard } from '../hooks/useTrustGuard';

const PilotOnboardingWizard = () => {
  const [currentStep, setCurrentStep] = useState(0);
  const [formData, setFormData] = useState({
    companyName: '',
    industry: '',
    riskTolerance: 'medium',
    desiredTier: 'standard'
  });
  const { verifyIdentity, getThreatScore } = useTrustGuard();

  const steps = [
    {
      id: 'identity',
      title: 'Enterprise Identity Verification',
      description: 'Securely verify your organization\'s identity to begin the pilot.',
      icon: <Lock className="w-6 h-6 text-ntrust-primary" />
    },
    {
      id: 'assessment',
      title: 'Security Posture Assessment',
      description: 'Evaluate your current security stance against industry benchmarks.',
      icon: <Shield className="w-6 h-6 text-ntrust-primary" />
    },
    {
      id: 'selection',
      title: 'Pilot Program Selection',
      description: 'Choose the security tier that best fits your operational needs.',
      icon: <CheckCircle className="w-6 h-6 text-ntrust-primary" />
    }
  ];

  const handleNext = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handleBack = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Simulate identity verification
    const verificationResult = await verifyIdentity(formData.companyName);
    if (verificationResult.success) {
      setCurrentStep(steps.length); // Move to success state
    }
  };

  if (currentStep === steps.length) {
    return (
      <div className="min-h-screen bg-ntrust-dark flex items-center justify-center p-6">
        <div className="bg-ntrust-surface rounded-2xl p-8 max-w-2xl w-full border border-ntrust-primary/20 shadow-2xl">
          <div className="flex justify-center mb-6">
            <div className="bg-green-500/20 p-4 rounded-full">
              <CheckCircle className="w-12 h-12 text-green-500" />
            </div>
          </div>
          <h2 className="text-3xl font-bold text-white text-center mb-4">
            Pilot Onboarding Complete
          </h2>
          <p className="text-gray-300 text-center mb-8">
            Welcome to nTrust. Your enterprise identity has been verified. 
            Your security dashboard is being provisioned.
          </p>
          <div className="bg-ntrust-dark/50 rounded-xl p-6 border border-gray-700">
            <h3 className="text-lg font-semibold text-white mb-3 flex items-center gap-2">
              <Shield className="w-5 h-5 text-ntrust-primary" />
              Next Steps
            </h3>
            <ul className="space-y-2 text-gray-300">
              <li className="flex items-start gap-2">
                <ChevronRight className="w-4 h-4 text-ntrust-primary mt-1" />
                <span>Access your provisional dashboard at <code className="bg-ntrust-dark px-2 py-1 rounded">dashboard.ntrust.ai</code></span>
              </li>
              <li className="flex items-start gap-2">
                <ChevronRight className="w-4 h-4 text-ntrust-primary mt-1" />
                <span>Complete your initial threat simulation within 24 hours</span>
              </li>
              <li className="flex items-start gap-2">
                <ChevronRight className="w-4 h-4 text-ntrust-primary mt-1" />
                <span>Review the SLA baseline document sent to your registered email</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-ntrust-dark flex items-center justify-center p-6">
      <div className="bg-ntrust-surface rounded-2xl p-8 max-w-3xl w-full border border-gray-700/50 shadow-2xl">
        {/* Progress Header */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-2xl font-bold text-white">{steps[currentStep].title}</h2>
            <div className="flex items-center gap-2 text-gray-400">
              <span className="text-sm">{currentStep + 1} of {steps.length}</span>
            </div>
          </div>
          <div className="w-full bg-gray-700 rounded-full h-2">
            <div 
              className="bg-ntrust-primary h-2 rounded-full transition-all duration-500"
              style={{ width: `${((currentStep + 1) / steps.length) * 100}%` }}
            ></div>
          </div>
          <p className="mt-4 text-gray-300">{steps[currentStep].description}</p>
        </div>

        {/* Step Content */}
        <div className="min-h-[300px]">
          {currentStep === 0 && (
            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Company/Organization Name
                </label>
                <input
                  type="text"
                  required
                  value={formData.companyName}
                  onChange={(e) => setFormData({...formData, companyName: e.target.value})}
                  className="w-full bg-ntrust-dark border border-gray-600 rounded-lg px-4 py-3 text-white focus:ring-2 focus:ring-ntrust-primary focus:border-transparent"
                  placeholder="e.g. Acme Corp"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Industry Sector
                </label>
                <select
                  required
                  value={formData.industry}
                  onChange={(e) => setFormData({...formData, industry: e.target.value})}
                  className="w-full bg-ntrust-dark border border-gray-600 rounded-lg px-4 py-3 text-white focus:ring-2 focus:ring-ntrust-primary focus:border-transparent"
                >
                  <option value="">Select your industry</option>
                  <option value="finance">Finance & Banking</option>
                  <option value="healthcare">Healthcare</option>
                  <option value="technology">Technology</option>
                  <option value="government">Government</option>
                  <option value="retail">Retail</option>
                  <option value="other">Other</option>
                </select>
              </div>
              <div className="flex justify-end pt-4">
                <button
                  type="submit"
                  className="bg-ntrust-primary hover:bg-ntrust-primary/90 text-white px-6 py-3 rounded-lg font-medium flex items-center gap-2 transition-colors"
                >
                  Verify Identity <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </form>
          )}

          {currentStep === 1 && (
            <div className="space-y-6">
              <div className="bg-ntrust-dark/50 rounded-xl p-6 border border-gray-700">
                <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
                  <AlertTriangle className="w-5 h-5 text-yellow-500" />
                  Risk Assessment
                </h3>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-300 mb-2">
                      Current Security Maturity Level
                    </label>
                    <div className="grid grid-cols-3 gap-3">
                      {['Basic', 'Intermediate', 'Advanced'].map((level) => (
                        <button
                          key={level}
                          onClick={() => setFormData({...formData, riskTolerance: level.toLowerCase()})}
                          className={`p-3 rounded-lg border ${
                            formData.riskTolerance === level.toLowerCase()
                              ? 'bg-ntrust-primary/20 border-ntrust-primary text-white'
                              : 'bg-ntrust-dark border-gray-600 text-gray-400 hover:border-gray-500'
                          } transition-colors`}
                        >
                          {level}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
              <div className="flex justify-between pt-4">
                <button
                  type="button"
                  onClick={handleBack}
                  className="text-gray-400 hover:text-white px-4 py-2"
                >
                  Back
                </button>
                <button
                  type="button"
                  onClick={handleNext}
                  className="bg-ntrust-primary hover:bg-ntrust-primary/90 text-white px-6 py-2 rounded-lg font-medium flex items-center gap-2 transition-colors"
                >
                  Next <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          )}

          {currentStep === 2 && (
            <div className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {[
                  { id: 'standard', name: 'Standard Pilot', price: '$2,500/mo', features: ['Basic Threat Monitoring', 'Weekly Reports', 'Email Support'] },
                  { id: 'enterprise', name: 'Enterprise Pilot', price: '$5,000/mo', features: ['Real-time Threat Intelligence', '24/7 Dedicated Support', 'Custom SLA', 'On-premise Deployment'] }
                ].map((tier) => (
                  <div
                    key={tier.id}
                    onClick={() => setFormData({...formData, desiredTier: tier.id})}
                    className={`bg-ntrust-dark/50 rounded-xl p-6 border-2 cursor-pointer transition-all ${
                      formData.desiredTier === tier.id
                        ? 'border-ntrust-primary bg-ntrust-primary/10'
                        : 'border-gray-700 hover:border-gray-600'
                    }`}
                  >
                    <h3 className="text-xl font-bold text-white mb-2">{tier.name}</h3>
                    <p className="text-2xl font-bold text-ntrust-primary mb-4">{tier.price}</p>
                    <ul className="space-y-2">
                      {tier.features.map((feature, idx) => (
                        <li key={idx} className="flex items-start gap-2 text-gray-300 text-sm">
                          <CheckCircle className="w-4 h-4 text-ntrust-primary mt-0.5" />
                          {feature}
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
              <div className="flex justify-between pt-4">
                <button
                  type="button"
                  onClick={handleBack}
                  className="text-gray-400 hover:text-white px-4 py-2"
                >
                  Back
                </button>
                <button
                  type="button"
                  onClick={handleNext}
                  className="bg-ntrust-primary hover:bg-ntrust-primary/90 text-white px-6 py-2 rounded-lg font-medium flex items-center gap-2 transition-colors"
                >
                  Complete Onboarding <CheckCircle className="w-4 h-4" />
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Step Indicators */}
        <div className="mt-8 flex justify-center gap-2">
          {steps.map((step, idx) => (
            <div
              key={step.id}
              className={`w-3 h-3 rounded-full transition-colors ${
                idx === currentStep ? 'bg-ntrust-primary' : idx < currentStep ? 'bg-ntrust-primary/50' : 'bg-gray-600'
              }`}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default PilotOnboardingWizard;