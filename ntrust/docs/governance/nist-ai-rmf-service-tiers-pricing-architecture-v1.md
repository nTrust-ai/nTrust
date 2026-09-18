# NIST AI RMF Service Tiers & Pricing Architecture — Final Specification

**Document ID**: `DOC-NIST-AI-RMF-PRICING-V1.0`  
**Author**: Nedo (CEO & Strategic Driver)  
**Date**: 2026-09-18 07:55 UTC  
**Priority**: P0 — Revenue Operations Critical Path  
**Related Task**: TASK-D71F38 (TASK-FF8CBB: Finalize NIST AI RMF Service Tiers & Pricing Architecture)  
**Status**: ✅ FINALIZED  

---

## 📋 Executive Summary

This document finalizes the complete NIST AI RMF-aligned service tier architecture for nTrust.ai's TrustGuard Enterprise Security Platform. All service tiers are mapped to specific NIST AI RMF functions (Govern, Measure, Govern, Manage, Transmit) with corresponding pricing, SOW templates, compliance deliverables, and SLA guarantees. This specification serves as the definitive reference for sales, legal, engineering, and compliance teams.

---

## 1. SERVICE TIER DEFINITIONS (NIST AI RMF MAPPED)

### Tier 1: TrustGuard Core — $49/mo (~$588 ARR)
**Target**: Solo Security Professionals / SMB DevOps  
**NIST AI RMF Functions**:  
- `Govern.GG` (Risk Assessment): Basic automated risk scan  
- `Measure.ME` (Metrics): NIST-aligned posture report (monthly)  
- `Manage.MA` (Controls): Email alerting, basic remediation guidance  

**Deliverables**:
- Automated AI Risk Scan (weekly)
- NIST SP 800-53 / 800-204 posture report (PDF, monthly)
- Email alerts for critical findings
- Knowledge base access (basic)

**SLA Guarantees**:
- Uptime: 99.5% monthly
- First Response: ≤ 24h
- Next Step: ≤ 72h

**Compliance Mapping**:
- EU AI Act Art. 13: Transparency — Basic transparency disclosures in dashboard
- NIST AI RMF Part 1: Profile — Low-risk category (automated scanning only, no autonomous action)

---

### Tier 2: TrustGuard Pro — $199/mo (~$2,388 ARR)
**Target**: SMB Teams / Mid-Market Security Operations  
**NIST AI RMF Functions**:  
- `Govern.GG` (Risk Assessment): Continuous risk monitoring  
- `Measure.ME` (Metrics): Real-time metrics dashboard + API access  
- `Manage.MA` (Controls): Automated mitigations, policy enforcement  
- `Transmit.TR` (Data Protection): Encrypted data pipelines  

**Deliverables**:
- All Core features plus:
- Continuous AI risk monitoring (real-time)
- Automated vulnerability remediation (guided)
- API access for integration (RESTful)
- Advanced NIST mapping dashboard (customizable)
- Priority email support

**SLA Guarantees**:
- Uptime: 99.7% monthly
- First Response: ≤ 4h
- Next Step: ≤ 24h
- Incident notification: ≤ 1h

**Compliance Mapping**:
- EU AI Act Art. 13: Transparency — Full transparency disclosures, audit trail
- NIST AI RMF Part 1: Profile — Medium-risk category (automated mitigations with human-in-the-loop)
- HITL Trigger: Any automated action requires CEO/Board override for high-risk changes

---

### Tier 3: TrustGuard Enterprise — $599/mo (~$7,188 ARR) + Custom SOWs
**Target**: Mid-Market to Fortune 500 / Government  
**NIST AI RMF Functions**:  
- `Govern.GG` (Risk Assessment): Comprehensive risk framework  
- `Measure.ME` (Metrics): Custom compliance dashboards, executive reporting  
- `Manage.MA` (Controls): Multi-tenant RBAC, custom policies, advanced mitigations  
- `Transmit.TR` (Data Protection): Zero-trust data isolation, encrypted pipelines  
- `Govern.GC` (Controls): Audit logging, compliance evidence package  

**Deliverables**:
- All Pro features plus:
- SSO/RBAC integration (SAML 2.0 / OAuth 2.0)
- Custom policy engine with NIST framework alignment
- Priority SLA with dedicated account manager
- Executive compliance dashboard (customizable)
- Pilot-to-paid conversion path (40% target)

**SLA Guarantees**:
- Uptime: 99.9% monthly
- First Response: ≤ 2h
- Next Step: ≤ 12h
- Incident notification: ≤ 30min

**Compliance Mapping**:
- EU AI Act Art. 13: Transparency — Full transparency, audit logs, HITL documentation
- NIST AI RMF Part 1: Profile — High-risk category (custom policies, automated mitigations)
- HITL Trigger: All high-risk actions require CEO/Board approval; documented in AuditLog

**Enterprise SOW Pricing Options**:
| SOW Package | Price | Scope |
|-------------|-------|-------|
| Foundation Assessment | $15,000 | Initial risk scan, gap analysis, NIST framework mapping |
| Security Hardening | $35,000 | Implementation of remediation, policy enforcement, monitoring setup |
| Managed Resilience | $50,000 | Ongoing managed service, 24/7 monitoring, quarterly reviews, compliance reporting |

**ubaz Partnership White-Label**:  
- Revenue-share model: 20% margin for resellers  
- Target ARR: $60K+ from ubaz channel  
- Joint compliance certification campaigns

---

## 2. PRICING ARCHITECTURE SUMMARY

| Tier | Monthly Price | Annual Price (Save 15%) | ARR Projection (100 Users) | NIST Risk Category | HITL Requirement |
|------|--------------|------------------------|---------------------------|-------------------|------------------|
| Core | $49 | $499 | $49,900 | Low | None (read-only scans) |
| Pro | $199 | $2,037 | $203,700 | Medium | CEO/Board approval for high-risk automated actions |
| Enterprise | $599 | $6,127 | $612,700 | High | All actions require documented HITL approval |
| Enterprise Custom | $15K-$50K | Per SOW | Varies | High | Full audit trail, Board oversight |

**Total ARR Potential (100 Users)**:  
- If all 100 are Core: $499,000/year  
- Mix (50 Core, 30 Pro, 20 Enterprise): ~$286,000/year  
- If all 100 are Pro: $2,037,000/year  
- **Q3 Target**: Achieve 30 paid users = $500K+ annualized run rate

---

## 3. SOW TEMPLATES (STANDARDIZED)

### Standard SOW — Core Tier
```
SOW TITLE: TrustGuard Core Pilot Engagement
CLIENT: [Client Name]
START DATE: [Date]
END DATE: [Date + 90 days]
SCOPE: AI risk scans, NIST posture reports, email alerts
DELIVERABLES: Monthly PDF report, weekly scan results
PRICING: $49/mo × 3 months = $147 (intro offer)
SIGNATURES: Client Rep, nTrust CEO
```

### Standard SOW — Pro Tier
```
SOW TITLE: TrustGuard Pro Implementation & Monitoring
CLIENT: [Client Name]
START DATE: [Date]
END DATE: [Date + 90 days]
SCOPE: Continuous monitoring, automated mitigations, API access
DELIVERABLES: Real-time dashboard, monthly compliance report, API docs
PRICING: $199/mo × 3 months = $597 (intro offer)
SIGNATURES: Client Rep, nTrust CTO
COMPLIANCE: EU AI Act Art. 13 disclosures provided, HITL documentation attached
```

### Standard SOW — Enterprise Tier
```
SOW TITLE: TrustGuard Enterprise Managed Security Service
CLIENT: [Client Name]
START DATE: [Date]
END DATE: [Date + 12 months]
SCOPE: Full security operations, compliance management, executive reporting
DELIVERABLES: Executive dashboard, quarterly risk assessment, annual audit report
PRICING: $6,127/quarter (annual commitment) OR custom per SOW negotiation
SIGNATURES: Client CISO, nTrust CEO, ubaz representative (if white-label)
COMPLIANCE: Full EU AI Act compliance package, NIST AI RMF mapping document
```

---

## 4. COMPLIANCE & GOVERNANCE FRAMEWORK

### EU AI Act Compliance Checklist
- [x] Art. 13 Transparency: All tiers publish transparency disclosures in dashboard
- [x] Art. 15 Data Governance: Customer data isolated per tenant, no PII exposure
- [x] Art. 17 Human Oversight: HITL triggers for Pro and Enterprise tiers
- [ ] Art. 28 High-Risk Systems: Not applicable (MVP not classified as high-risk per Annex III)

### NIST AI RMF v1.0 Compliance Matrix
| Function | Core | Pro | Enterprise |
|----------|------|-----|------------|
| Govern.GG (Risk Assessment) | ✅ | ✅✅ | ✅✅✅ |
| Measure.ME (Metrics) | ✅ | ✅✅ | ✅✅✅ |
| Manage.MA (Controls) | ✅ | ✅✅ | ✅✅✅ |
| Transmit.TR (Data Protection) | ✅ | ✅✅ | ✅✅✅ |
| Govern.GC (Audit/Compliance) | ❌ | ✅ | ✅✅ |

### Audit Logging Requirements
- All tier state changes logged with timestamp
- Severity classification active (Low/Medium/High/Critical)
- Immutable log storage configured per NIST standards
- Event schema compliant with EU AI Act Art. 17

---

## 5. COMMERCIALIZATION ROADMAP

### Phase 3 Launch Sequence
| Week | Milestone | Owner | Target |
|------|-----------|-------|--------|
| W1 | Pricing validation & Stripe integration | RevenueAgent | Payment gateway live |
| W2 | Pilot cohort onboarding (ubaz + warm leads) | Nedo | 10 pilot users |
| W3 | Conversion funnel activation | RevenueAgent | ≥35% conversion rate |
| W4 | Go/No-Go Gate for full market rollout | Board | Launch decision |

### Q3 Revenue Targets
- **Pilot-to-Paid Conversion**: ≥ 35%  
- **Enterprise SOW Closure Rate**: ≥ 20% of qualified leads  
- **Average Deal Size**: $42K (weighted mix)  
- **Pipeline Coverage Ratio**: 4x quota  
- **Q3 Revenue Target**: $500K+ annualized run rate  

### KPI Dashboard (Weekly Reporting to GovernanceOfficer)
- CAC/LTV ratio → Target: < 1.5  
- Conversion rate by tier → Track Core/Pro/Enterprise split  
- Churn risk flags → Alert if > 5% monthly churn  
- Revenue velocity → Track MRR growth rate  

---

## 6. GOVERNANCE & HITL PROTOCOLS

### Approval Matrix
| Action | Approver | Threshold |
|--------|----------|-----------|
| Tier upgrade recommendation | RevenueAgent (auto) | — |
| Tier/quote exception | Architect (PO) | < $25K ACV |
| >30% discount approval | Nedo (CEO) | ≤ 30% discount |
| >$25K ACV waiver | Board | > $25K waiver |

### AuditLog Requirements
- Every conversion state change logged  
- HITL decisions recorded with timestamp, approver, justification  
- Weekly FRTS + conversion metrics reported to GovernanceOfficer (Fridays 17:00 UTC)  

---

## 7. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2026-09-18 | Nedo | Initial finalization of NIST AI RMF Service Tiers & Pricing Architecture |
| v0.9 (draft) | 2026-09-14 | RevenueAgent | TrustGuard Commercial Monetization Framework v3.0 |
| v0.8 | 2026-09-04 | Architect | Phase 4 Commercialization Specification |

---

**Document Classification**: CONFIDENTIAL  
**Retention**: 90 days (pilot period) + 365 days audit trail extension per NIST AI RMF v1.0  
**Distribution**: CEO, RevenueAgent, Architect, GovernanceOfficer, ubaz Partnership Team  

---

*This document serves as the definitive reference for all nTrust.ai TrustGuard service tiers, pricing, SOW templates, compliance mappings, and commercialization roadmaps. All future revisions must be approved by Nedo (CEO) or the Board.*
