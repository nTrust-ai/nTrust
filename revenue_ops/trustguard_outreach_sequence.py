"""
nTrust.ai — TrustGuard Tiered Pricing Outreach Sequence v1.0
Executes MEDDIC-aligned outbound/inbound follow-ups per FRTS SLA.
Tiers: Starter ($49/mo), Pro ($199/mo), Enterprise (Custom $15K/$35K/$50K SOW)
"""

outreach_sequence = [
    {
        "day": 0,
        "action": "Initial Qualification & SLA Ack",
        "template": "Thank you for your inquiry. Per our FRTS v1.0 intake protocol, we've logged your request and will provide a tailored risk assessment within 24 hours. Which TrustGuard tier aligns with your current compliance maturity?",
        "target": "All inbound leads"
    },
    {
        "day": 1,
        "action": "MEDDIC Deep-Dive",
        "template": "Following up on your security posture assessment. To map the correct TrustGuard tier ($49/$199/$599 or Enterprise SOW), we need to validate: 1) Decision criteria, 2) Economic buyer contact, 3) Current pain metrics.",
        "target": "Qualified leads"
    },
    {
        "day": 3,
        "action": "Pilot Conversion Offer",
        "template": "We're ready to deploy your sandboxed TrustGuard pilot. This validates our AI-compliance engine against your specific threat landscape. Pilot-to-paid conversion path is now open.",
        "target": "High-intent prospects"
    },
    {
        "day": 7,
        "action": "Enterprise SOW Escalation",
        "template": "For organizations requiring custom architecture reviews and NIST AI RMF alignment, our Enterprise SOW brackets ($15K/$35K/$50K) are now available for Q3-Q4 deployment.",
        "target": "C-Suite/CTO prospects"
    }
]

def execute_sequence(lead_id):
    print(f"Executing TrustGuard outreach sequence for {lead_id}...")
    for step in outreach_sequence:
        print(f"[Day {step['day']}] {step['action']} -> {step['template'][:50]}...")
    return "SEQUENCE_DEPLOYED"

execute_sequence("LEAD-Q3-001")
