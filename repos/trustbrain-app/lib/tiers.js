// TrustBrain™ tier entitlement matrix & pricing (source of truth for Portal UI + /api/tiers)
// Illustrative pricing per TASK-TB-001 §5 — revenue lever = connector count × tier.

export const TIERS = [
  {
    id: 'community',
    name: 'Community',
    tagline: 'Free — bottom-up adoption funnel',
    price: '$0',
    period: 'forever',
    connectors: 3,
    features: {
      reasoningCore: true,
      iacGeneration: false,
      tokenShield: false,
      autonomousExecution: 'limited',
      auditLedger: 'basic',
      sla: null
    },
    highlight: false
  },
  {
    id: 'standard',
    name: 'Standard',
    tagline: 'Solo analysts & small teams',
    price: '$49',
    period: '/node/mo',
    connectors: 10,
    features: {
      reasoningCore: true,
      iacGeneration: false,
      tokenShield: false,
      autonomousExecution: 'limited',
      auditLedger: 'basic',
      sla: null
    },
    highlight: false
  },
  {
    id: 'professional',
    name: 'Professional',
    tagline: 'Core monetization unit',
    price: '$299',
    period: '/node/mo',
    connectors: 25,
    features: {
      reasoningCore: true,
      iacGeneration: true,
      tokenShield: true,
      autonomousExecution: true,
      auditLedger: true,
      sla: '99.9%'
    },
    highlight: true
  },
  {
    id: 'enterprise',
    name: 'Enterprise',
    tagline: 'Platform license + connector uplift',
    price: 'Custom',
    period: '/yr',
    connectors: '∞',
    features: {
      reasoningCore: true,
      iacGeneration: true,
      tokenShield: true,
      autonomousExecution: true,
      auditLedger: true,
      sla: '99.95%'
    },
    highlight: false
  },
  {
    id: 'elite',
    name: 'Elite',
    tagline: 'MSSP multi-tenant rights',
    price: 'Negotiated',
    period: '/yr',
    connectors: '∞',
    features: {
      reasoningCore: true,
      iacGeneration: true,
      tokenShield: true,
      autonomousExecution: true,
      auditLedger: true,
      sla: '99.99% + premium support'
    },
    highlight: false
  }
]

export const DIFFERENTIATORS = [
  { title: 'Privacy-Preserving Inference', body: 'TokenShield™ Zero-Knowledge Gateway — surrogate tokenization + local restore, so infrastructure secrets never leave the tenant boundary.' },
  { title: 'Reversible-by-Design', body: 'Deterministic rollback commands on every playbook. The Governor hard-denies any remediation lacking a verifiable undo path.' },
  { title: 'Human-in-the-Loop by Policy', body: 'Configurable blast-radius threshold + sensitive-keyword triggers escalate to a HITL queue automatically.' },
  { title: 'Multi-Format Output', body: 'Terraform/OpenTofu IaC, hardened Bash, and Python SDK automation — every playbook embeds rollback instructions.' },
  { title: 'Cryptographic Audit Ledger', body: 'Tamper-evident SHA-256 block chain satisfying EU AI Act Art. 12 traceability and NIST AI RMF MEASURE/MANAGE.' },
  { title: 'Cross-Product Blast Radius', body: 'Reasons across TrustGuard, Shield, PrivacyGuard, TrustAudit, AppSec, and TokenShield — a graph no single-vendor copilot can span.' }
]

export const MITRE = ['T1003.001 · LSASS Dumping', 'T1486 · Data Encrypted for Impact', 'T1567 · Exfiltration Over Web Service']
export const FRAMEWORKS = ['CIS v2.0', 'NIST 800-53 CM-2', 'ISO 27001 A.12.1.2', 'PCI-DSS 4.0', 'SOC 2', 'HIPAA', 'GDPR', 'EU AI Act', 'NIS2']

export const INSTALL_COMMAND = 'curl -fsSL https://trustbrain.ntrust.ai/install.sh | bash'
