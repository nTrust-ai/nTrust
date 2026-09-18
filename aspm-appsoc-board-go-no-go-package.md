# 🛡️ nTrust.ai — ASPM/AppSOC Board Go/No-Go Decision Package

**Task**: TASK-FD8964 | **Goal**: GOAL-D89467 ($500K+ Q3 Target)  
**Prepared by**: Nedo, CEO | **Date**: 2026-09-16 UTC  
**Decision Deadline**: October 3, 2026  

---

## 📋 EXECUTIVE SUMMARY

This document provides the Board with a comprehensive evidence package and recommendation for the ASPM (Application Security Posture Management) / AppSOC (Application Security Operations Center) product launch decision. This is a **Go/No-Go** gate that determines whether nTrust.ai proceeds to commercialize its enterprise security services in Q4 2026.

**Current Status**: ASPM/AppSOC listed as "Coming Soon" on the public nTrust.ai site — not yet available for paid SOW execution.

**Board Decision Required**: GO or NO-GO for ASPM/AppSOC commercial launch by October 3, 2026.

---

## 1. PRODUCT OVERVIEW

### 1.1 What Is ASPM/AppSOC?
- **ASPM (Application Security Posture Management)**: Automated security posture assessment, vulnerability management, and compliance monitoring for enterprise applications.
- **AppSOC (Application Security Operations Center)**: 24/7 application security monitoring, incident response, and managed detection services.

### 1.2 Tier Structure (Validated)
| Tier | ACV | Target Customer | Delivery Model |
|------|-----|-----------------|----------------|
| ASPM Essentials | $24,000 | Mid-market, entry-level | Automated triage + runbook orchestration |
| ASPM Pro | $54,000 | Growth-stage enterprise | Enhanced automation + senior oversight |
| AppSOC Command | $108,000 | Regulated industries (PCI DSS, DORA, SEC) | 24/7 automated monitoring + on-call escalation |

---

## 2. ECONOMIC VALIDATION SUMMARY

*Source: doc_ef219494bc — ASPM/AppSOC Tier Economics Validation Report v1.0 (Architect, 2026-09-04)*

### 2.1 Key Metrics
| Metric | Value | Status |
|--------|-------|--------|
| Blended ACV (Target Mix B) | $57,000 | ACHIEVABLE |
| Gross Margin (Year-1) | ~58.3% | Above 55% threshold |
| Pilot-to-Paid Conversion | >=70% | Plausible (mirrors TrustGuard 78.2%) |
| ubaz Partner Margin | 20% net-positive | Confirmed with cap |

### 2.2 Year-1 Net Contribution Scenarios
| Scenario | Accounts | Net Contribution | Verdict |
|----------|----------|------------------|---------|
| B -- 15 accounts (entry-skewed) | 15 | ~$331K | Below $500K target |
| B -- 20 accounts | 20 | ~$458K | Close, needs steering |
| C -- 18 regulated-heavy accounts | 18 | ~$481K | Approaching target |
| **C -- 20 direct-sourced accounts** | **20** | **~$618K** | **Exceeds $500K** |

### 2.3 Critical Economic Constraints
1. **AppSOC "24/7" cannot fund staffed SOC**: Must be automated monitoring + on-call escalation (<=15-min response), NOT 24/7 human staffing. Otherwise GM collapses below 20%.
2. **Mix steering is mandatory**: >=25% Command tier for blended ACV >=$55K. Essentials = upsell wedge only, not volume driver.
3. **Partner-sourced cap <=40%**: Protects blended margin from channel concentration risk.

---

## 3. GO/NO-GO CONDITIONS CHECKLIST

*All conditions must be satisfied for a "GO" decision:*

| # | Condition | Status | Notes |
|---|-----------|--------|-------|
| 1 | Automation-first delivery (L1 auto-triage + runbook orchestration) | PENDING | Delivery stack under development; non-negotiable to hold >=55% GM |
| 2 | SOW scope & SLA discipline defined | DRAFTED | Guardrails documented in validation report |
| 3 | Capacity cap: <=5 concurrent pilots | ACCEPTABLE | Delivery talent scarcity per NIST AI RMF MP/ME |
| 4 | Mix steering enforcement mechanism | PENDING | Sales motion must steer regulated buyers to Command tier |
| 5 | Pilot discount guardrail (30% off Tier-1, max 3 pilots) | DOCUMENTED | At $16.8K ACV vs $9.2K COGS = 45% GM (acceptable for validation) |
| 6 | Per-account delivery telemetry capture | PENDING | Required to validate GM model vs reality pre-launch |
| 7 | Channel cap: ubaz-sourced <=40% of bookings | GUARDRAILED | Policy documented; enforcement mechanism needed |

**Overall Condition Compliance**: 3/7 fully met, 1 drafted, 3 pending/in-development.

---

## 4. RISK ASSESSMENT

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Delivery capacity shortfall vs. demand | High | Medium | <=5 pilot cap; contractor flex pool; staged rollout |
| Margin erosion from scope creep | High | Medium | Strict SOW guardrails; change-order process; tool/integration caps |
| Regulatory compliance gap (EU AI Act, NIST RMF) | Critical | Low-Medium | Compliance documentation in progress; GovernanceOfficer engagement active |
| Partner concentration risk (ubaz >40%) | Medium | Medium | Channel cap policy; direct-sourced mix target >=60% |
| Pilot-to-paid conversion below target | Medium | Low-Medium | Mirrors TrustGuard's 78.2%; intro discount capped at 30% for 90 days |

---

## 5. COMPARATIVE REVENUE ANALYSIS (ASPM/AppSOC vs. TrustGuard SaaS)

| Metric | ASPM/AppSOC (Services) | TrustGuard (SaaS) |
|--------|------------------------|-------------------|
| Gross Margin | ~40-58% (delivery-dependent) | ~85% (software margin) |
| Year-1 Net Contribution | $350-618K (scenario-dependent) | Proven model, scaling |
| Time to Revenue | 60-90 days (pilot -> SOW) | Immediate (self-serve) |
| Delivery Complexity | High (managed service) | Low (SaaS platform) |
| Scalability | Constrained by FTE capacity | Unlimited (software) |
| Compliance Burden | High (EU AI Act, NIST RMF) | Moderate |

**CEO Assessment**: Services GM ~40% vs. SaaS GM ~85% favors TrustGuard SaaS + Enterprise Audit SOWs for Q3 2026 revenue. ASPM/AppSOC is a strategic Q4 play that requires delivery infrastructure readiness before commercial launch.

---

## 6. BOARD RECOMMENDATION

### **Recommendation: CONDITIONAL GO with Q4 Launch Timeline**

**Rationale**:
1. **Economic viability confirmed**: Tier economics are validated (>=55% GM achievable at target mix). Year-1 net contribution of $350-618K is accretive to the $500K+ organizational mission, even if base case ($350-450K) falls short of the standalone $500K threshold.
2. **Strategic positioning**: ASPM/AppSOC fills a critical gap in nTrust.ai's enterprise security portfolio alongside TrustGuard SaaS and Enterprise Security Audit services. This creates a complete security stack offering for regulated industries.
3. **Q3 is too late for launch**: Given the current state of delivery infrastructure (automation-first stack under development), a Q3 commercial launch would risk margin erosion and compliance gaps. A Q4 launch (starting October 1) with a November pilot cohort is more realistic.
4. **Compliance documentation**: NIST AI RMF and EU AI Act evidence packages are in progress but not yet complete. These must be finalized before any paid SOW execution begins.

### **Go Conditions That Must Be Met Before Q4 Launch**
1. Automation-first delivery stack validated (target: September 30)
2. SOW templates for all three tiers finalized and Board-approved (target: September 25)
3. Compliance evidence package (NIST AI RMF + EU AI Act) complete (target: October 1)
4. Pilot cohort of <=5 accounts identified and Board-committed (target: October 10)
5. Telemetry capture mechanism deployed for per-account delivery hour tracking

### **If No-Go Decision**
- Retain "Coming Soon" status on nTrust.ai indefinitely or until Q1 2027
- Reallocate delivery capacity to TrustGuard SaaS and Enterprise Audit SOWs (higher margin, faster revenue)
- Revisit ASPM/AppSOC launch in H1 2027 with revised economic model

---

## 7. ACTION ITEMS FOR BOARD DISPOSITION

| # | Action | Owner | Target Date |
|----|--------|---------|-------------|
| 1 | Make GO or NO-GO decision on ASPM/AppSOC commercial launch | Board (Naveed) | October 3, 2026 |
| 2 | If GO: Approve Q4 pilot cohort of <=5 accounts | Board + RevenueAgent | October 10, 2026 |
| 3 | If GO: Finalize and publish SOW templates for all three tiers | Architect + GovernanceOfficer | September 25, 2026 |
| 4 | If NO-GO: Update nTrust.ai to remove "Coming Soon" ASPM/AppSOC references or set new launch date | Weaver (Dev) | October 5, 2026 |
| 5 | If GO: Begin Q4 delivery infrastructure build-out (automation stack, telemetry) | Architect + Atlas | October 1, 2026 |

---

## 8. APPENDIX: Cross-Reference Documents

| Document ID | Title | Relevance |
|-------------|-------|-----------|
| doc_ef219494bc | ASPM/AppSOC Tier Economics Validation Report v1.0 | Core economic validation evidence |
| doc_17a040df87 | NTRUST-RISK-ASSESSMENT-PHASE3-REVENUE-V1.0.md | Phase 3 revenue risk register |
| doc_1c666c1959 | CEO Watch Log AUDIT-0E19B0 (v6) | Board HITL tracking; ASPM/AppSOC "Coming Soon" status confirmed |
| doc_fcf756cebf | Governance Compliance & Pilot Readiness Status Update (v2.0) | Pilot readiness evidence |
| doc_43c9e2409e v2 | CEO Host-Vantage Verification Certificate | Infrastructure readiness evidence |

---

*Prepared by Nedo, CEO -- nTrust.ai*  
*"It is the numbers we trust."*  
**Classification**: Internal Use Only -- Board & Executive Access Required
