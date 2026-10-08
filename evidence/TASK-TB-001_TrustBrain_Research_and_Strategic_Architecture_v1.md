# 🧠 TrustBrain™ — Research & Strategic Architecture for the Autonomous Security Reasoning Copilot

**Document ID:** TASK-TB-001
**Owner:** Nedo (CEO), nTrust.ai
**Date:** 2026-10-07
**Classification:** Internal — Strategic Architecture Standard
**Product Pillar:** Pillar 1 (Core Engine) — `nTrust-ai/trustbrain`
**Related Standards:** ARCH-NT-004 (4-Pillar Autonomous Product Lifecycle), Core DNA v8.0
**Verification Snapshot:** 12/12 engine tests passing @ 2026-10-07T01:10:59Z

---

## 1. Executive Summary

TrustBrain™ is the **reasoning layer** of the nTrust sovereign cybersecurity suite. Where the other
engines *detect* (TrustGuard drift, Shield threats, PrivacyGuard PII exposure), TrustBrain™ *reasons*
about what a finding means, predicts its blast radius across systems, and produces a **safe, reversible,
multi-format remediation playbook** — while guaranteeing that no sensitive infrastructure data ever
leaves the tenant boundary in the clear.

This document consolidates (a) market research on the AI-SOC / security-copilot segment,
(b) the strategic positioning and portfolio synergy for TrustBrain™, (c) the concrete technical
architecture as implemented in `nTrust-ai/trustbrain`, (d) the monetization and licensing model,
(e) a delivery roadmap, and (f) the empirical verification ledger.

**Strategic Thesis:** The AI-copilot market is crowded *horizontally* but empty *vertically* for a
privacy-preserving, reversible-by-design, cross-product reasoning engine that a regulated mid-market
buyer can deploy **on its own infrastructure without shipping telemetry to a hyperscaler**. That is the
nTrust wedge.

---

## 2. Strategic Context & Market Research

### 2.1 The AI-SOC Inflection Point
Security Operations Centers are structurally capacity-constrained: alert volume grows faster than
analyst headcount, and the mean time-to-respond is dominated by *reasoning* (triage + correlation +
remediation authoring), not detection. The industry's response since 2023 has been the
"security copilot": an LLM-augmented layer that ingests findings and proposes analyst actions.

Two market truths shape our strategy:

1. **Detection is commoditized; reasoning is the moat.** Rules, scanners, and CSPM engines are
   abundant. The scarce good is trustworthy reasoning that an auditor will accept.
2. **Privacy is the unsolved blocker for regulated buyers.** Every major copilot routes telemetry to a
   vendor cloud. Banks, healthcare, defense-adjacent, and EU publics are contractually and legally
   barred from doing so. Whoever solves *zero-knowledge reasoning* unlocks the largest unserved
   segment.

### 2.2 Competitive Landscape

| Player | Category | Reasoning Model | Data Locality | Reversibility / Guardrails | Gap vs. TrustBrain™ |
|---|---|---|---|---|---|
| Microsoft Security Copilot | Copilot | GPT-family, vendor cloud | Vendor cloud only | Prompt-based, no deterministic rollback | No zero-knowledge mode; locked to M365/Defender telemetry |
| Google SecOps + Gemini | Copilot | Gemini, vendor cloud | Google cloud | Agentic actions, limited rollback UX | No on-prem privacy gateway; Google-native only |
| Palo Alto Cortex XSIAM | Platform | Proprietary ML | Vendor cloud | Automated response via playbooks | Heavier platform lock-in; no privacy WAF |
| CrowdStrike Charlotte AI / Falcon | Copilot | Proprietary LLM | Vendor cloud | Guided response | EDR-centric; cannot reason across non-CrowdStrike estates |
| SentinelOne Purple AI | Copilot | Proprietary LLM | Vendor cloud | Guided response | EDR/XDR-centric |
| Dropzone AI / Radiant / Intezer AI SOC | AI-SOC analysts | LLM triage | Vendor cloud | Ticket triage focus | Triage-only; no remediation authoring, no reversibility contract |
| Torq / Tines / Swimlane | SOAR | Workflow, some LLM | Self-hostable | Playbook execution | Orchestration, not reasoning; no blast-radius graph |
| **TrustBrain™ (nTrust.ai)** | **Reasoning copilot** | **Dual-Agent (Worker + Governor)** | **On-prem / tenant-owned; TokenShield zero-knowledge gateway** | **Reversibility-by-design: no rollback ⇒ policy-denied; HITL thresholds; SHA-256 audit chain** | — |

### 2.3 Gap Analysis & nTrust Right-to-Win
- **Zero-Knowledge Reasoning** (TokenShield™): infrastructure identifiers (RFC1918 CIDRs, credentials,
  API keys, PII) are replaced with synthetic surrogates *before* any model inference and restored
  locally during playbook compilation. No competitor ships this as a first-class gateway.
- **Sovereign Deployment**: the engine runs as a standalone OCI container (port 8092) on the customer's
  own infrastructure. No data egress required.
- **Reversibility Contract**: the Governor agent hard-denies any remediation that lacks a verifiable
  rollback path — turning "AI did something scary" into "AI produced an auditable, undoable change."
- **Cross-Product Blast Radius**: TrustBrain reasons across **all seven** nTrust engines, a
  graph no single-vendor copilot can span.

---

## 3. Product Strategy & Positioning

### 3.1 Positioning Statement
> *For security and platform teams in regulated enterprises who cannot ship telemetry to a vendor
> cloud, TrustBrain™ is the sovereign reasoning copilot that turns a raw finding into a verified,
> reversible, multi-format remediation playbook — without ever exposing infrastructure secrets.*

### 3.2 Core Differentiators
1. **Privacy-Preserving Inference** — TokenShield Zero-Knowledge Gateway (surrogate tokenization + local restore).
2. **Reversible-by-Design** — deterministic rollback commands; Governor denies irreversible actions.
3. **Human-in-the-Loop by Policy** — configurable blast-radius threshold + sensitive-keyword triggers.
4. **Multi-Format Output** — Terraform/OpenTofu IaC, hardened Bash, Python SDK automation.
5. **Cryptographic Audit Ledger** — tamper-evident SHA-256 block chain (EU AI Act Art. 12 traceability).
6. **Suite Correlations** — reasons across TrustGuard, Shield, PrivacyGuard, TrustAudit, AppSec, TokenShield.

### 3.3 Target Segments (ICP)
| Segment | Pain | Trigger |
|---|---|---|
| Regulated mid-market (50–2,000 staff) | No SOC budget; auditor demands evidence | ISO 27001 / SOC 2 readiness |
| EU / data-sovereignty buyers | GDPR Art. 32/33; no third-country transfer | DPIA / breach readiness |
| MSPs & MSSPs | Margin pressure; must scale analysis | Multi-tenant hardening mandates |
| Platform / DevOps teams | Config drift → outages | Cloud migrations (Azure/AWS/GCP) |

### 3.4 Portfolio Synergy (the "nTrust Reasoning Spine")
TrustBrain™ is the connective tissue across the product suite:

```
TrustGuard™ (drift) ─┐
nTrust Shield™ (threat) ─┐
PrivacyGuard™ (PII) ─┼──▶  TrustBrain™  ──▶  Reversible Playbook  ──▶  TrustAudit™ (evidence)
Managed AppSec ─┘        (Worker + Governor)         │
Enterprise Audit ─┘                                   ▼
                                              Cryptographic Ledger
```

---

## 4. Technical Architecture

### 4.1 4-Pillar Topology (per ARCH-NT-004)
| Pillar | TrustBrain™ Implementation |
|---|---|
| **P1 — Core Engine** | `nTrust-ai/trustbrain` standalone repo, OCI container, port **8092**, FastAPI + SQLite |
| **P2 — Licensing/Installer Hub** | `portal.ntrust.ai/trustbrain`, one-line installer, Lemon Squeezy webhooks (roadmap) |
| **P3 — Marketing** | `ntrust.ai/products/trustbrain` feature page & demo (roadmap) |
| **P4 — Agent Governance** | Managed autonomously by nTrust org (Nedo/Atlas/Weaver/SRE) |

### 4.2 Dual-Agent Core (Spine Sovereign Architecture)
- **TrustBrain Worker Agent** — reasoning, synthesis, remediation playbook + rollback authoring.
  Public surface: `explain_finding()`, `correlate_blast_radius()`, `generate_playbook()`.
- **TrustBrain Governor Agent** — policy verification, HITL triggering, cryptographic audit ledger,
  rollback determinism (`TrustBrainGovernor`).
- **Design principle:** separation of *proposal* (Worker) from *authorization* (Governor) is the
  agentic analogue of Separation of Duties and is the control that makes autonomous remediation
  defensible to an auditor.

### 4.3 TokenShield™ Zero-Knowledge Privacy Gateway
`TokenShieldSanitizer.sanitize(text) -> (sanitized_text, vault, count)`
- Regex/NLP detectors for: internal IPv4/IPv6 CIDRs, emails, API keys (`sk-*`), credentials, PII.
- Sensitive spans replaced with surrogate tokens (`[INTERNAL_SUBNET_n]`, `[TOKENSHIELD_SECRET_n]`,
  `[ANONYMIZED_USER_n@corp.internal]`).
- Vault retained locally; surrogates restored during playbook compilation.
- **Verified:** input containing `naveed@ntrust.ai`, `sk-proj-…`, `10.0.0.4` yields 3 redactions and
  `ZERO_KNOWLEDGE_PRESERVED`.

### 4.4 Blast-Radius Correlation Engine
- Models upstream/downstream dependencies across Azure, Plesk, network firewalls, and SecOps agents.
- Emits a quantitative **Blast Radius Score (0–100)** and level (`LOW / HIGH / CRITICAL`).
- Maps findings to **MITRE ATT&CK Enterprise v14.1** techniques (e.g. `T1003.001` LSASS dumping,
  `T1486` data-encrypted-for-impact, `T1567` exfiltration-over-web-service).
- Maps to compliance frameworks: CIS v2.0, NIST 800-53 CM-2, ISO 27001 A.12.1.2, PCI-DSS 4.0,
  SOC 2, HIPAA, GDPR, EU AI Act Art. 12/14, NIS2.

### 4.5 Multi-Format Remediation Playbook Generator
`generate_playbook(finding, fmt=…, product_id=…)` produces:
- **Terraform / OpenTofu** — declarative HCL with `plan -target` dry-run + rollback.
- **Hardened Bash** — `set -euo pipefail`, verification checks, rollback block.
- **Python SDK** — programmatic remediation with error handling + dry-run flag.
Every playbook embeds explicit **rollback instructions**.

### 4.6 Governance: Reversibility & HITL
`POST /api/v1/governance/evaluate` returns one of:
- `AUTONOMOUS_APPROVED` — risk below threshold, reversible.
- `HITL_REQUIRED` — risk ≥ threshold, or sensitive keyword detected.
- `POLICY_DENIED` — **no rollback path** ⇒ never executable.
Config is agent-tunable at runtime (`/api/v1/config`): `hitl_blast_threshold`,
`autonomous_execution_allowed`, `sensitive_keywords`.

### 4.7 Cryptographic Audit Ledger
- Append-only `cryptographic_audit_ledger` (SHA-256 block chain, prev-hash linkage).
- `verify_audit_chain_integrity()` proves the chain is unbroken and emits an ISO 27001 attestation.
- Satisfies EU AI Act Art. 12 (record-keeping) and NIST AI RMF MEASURE/MANAGE controls.

### 4.8 API Surface (v1)
| Method | Path | Purpose |
|---|---|---|
| GET | `/api/v1/health` | Liveness + product connectivity + privacy-shield status |
| GET | `/api/v1/products` | Catalogue of the 7 connected engines |
| GET | `/api/v1/status` | Engine + governor state |
| POST | `/api/v1/explain` | Explain a single finding (blast radius, MITRE) |
| POST | `/api/v1/synthesize` | Full reasoning → playbooks → governor verdict |
| POST | `/api/v1/generate-playbook` | Multi-format playbook generation |
| POST | `/api/v1/execute-playbook` | Execute with reversibility guarantee |
| POST | `/api/v1/governance/evaluate` | Worker proposal → Governor verdict |
| GET | `/api/v1/governance/approvals` | Pending HITL queue |
| POST | `/api/v1/governance/resolve` | Approve/Reject (SoD: decider identity required) |
| GET | `/api/v1/governance/audit-chain` | Chain + integrity attestation |
| POST | `/api/v1/governance/rollback` | Deterministic rollback execution |
| POST | `/api/v1/sanitize` | TokenShield zero-knowledge sanitization |
| GET/POST | `/api/v1/config` | Agent-tunable policy configuration |
| GET | `/api/v1/audit/logs` | Immutable audit trail |

### 4.9 Data Model (SQLite)
`config_baselines`, `drift_events`, `connectors`, `audit_logs`, `offline_audits`, `users`,
`cryptographic_audit_ledger`, `governance_approvals`.

---

## 5. Monetization & Licensing

### 5.1 Tier Entitlement Matrix
| Capability | Community | Standard | Professional | Enterprise | Elite |
|---|---|---|---|---|---|
| Max connectors | 3 | 10 | 25 | ∞ | ∞ |
| TrustBrain reasoning core | ✅ | ✅ | ✅ | ✅ | ✅ |
| Terraform/IaC generation | ❌ | ❌ | ✅ | ✅ | ✅ |
| TokenShield WAF gateway | ❌ | ❌ | ✅ | ✅ | ✅ |
| Autonomous execution | limited | limited | ✅ | ✅ | ✅ |
| Audit ledger / SLA | basic | basic | ✅ | ✅ | ✅ |

### 5.2 Pricing & Revenue Model (illustrative)
- **Community** — free (funnel / bottom-up adoption).
- **Professional** — per-node annual subscription (~$Xk/yr) — the core monetization unit.
- **Enterprise** — platform license + connector-based uplift + premium support.
- **Elite** — negotiated, MSSP multi-tenant rights.
**Primary revenue lever:** connector count × tier, mirroring the TrustGuard licensing rails (single
entitlement backbone → lower support cost, faster upsell).

---

## 6. Delivery Roadmap

| Phase | Objective | Status |
|---|---|---|
| **TB-0** | Engine, Governor, TokenShield, playbooks, ledger, tests | ✅ **Complete (12/12 green)** |
| **TB-1** | Real LLM reasoning core wiring (pluggable model router) + TokenShield gateway proxy | Planned |
| **TB-2** | Portal licensing + one-line installer (`portal.ntrust.ai/trustbrain`) | Planned |
| **TB-3** | Marketing feature page & live demo (`ntrust.ai/products/trustbrain`) | Planned |
| **TB-4** | Design-partner pilots; SOC 2 / EU AI Act evidence pack | Planned |

---

## 7. Risk Register (RAID)

| ID | Type | Risk | Impact | Mitigation |
|---|---|---|---|---|
| TB-R1 | Risk | LLM hallucination in remediation code | High | Governor + deterministic rollback + HITL |
| TB-R2 | Risk | Sensitive-data leakage to model provider | Critical | TokenShield zero-knowledge gateway (pre-inference) |
| TB-R3 | Risk | Repo outside Spine sandbox / git tooling gap in sandbox | Medium | ARCH-NT-004 `/app/data/repos` mount + host sync |
| TB-R4 | Assumption | Buyers accept self-hosted container model | Medium | Ship managed option at Elite tier |
| TB-R5 | Issue | Concurrent development on engine files | Low | Path-scoped commits; strategy owned by CEO (this doc) |

---

## 8. KPIs & Success Metrics
- **Adoption:** installs / week; active connectors.
- **Value:** findings auto-triaged; mean-time-to-remediation reduction.
- **Trust:** % remediations with verified rollback (target 100%); audit-chain integrity (target 100%).
- **Revenue:** ARR from Professional/Enterprise tiers; expansion via connector growth.

---

## 9. Empirical Verification Appendix
- **Test suite:** 12/12 passing @ `2026-10-07T01:10:59Z` (health, governor HITL/autonomous/deny,
  HITL lifecycle, audit-chain integrity, rollback determinism, tunable config, rejection lifecycle,
  7-product synthesis, sensitive-keyword trigger, TokenShield sanitizer).
- **Runtime:** Python 3.11.15, FastAPI 0.142.2, Pydantic 2.13.5.
- **Repo:** `nTrust-ai/trustbrain` @ `e0d51b2` (P1 engine), container port 8092.
- **Note:** the engine repo is under active development by a peer worker; the snapshot above is the
  authoritative state at the timestamp noted.

---

## 10. Governance & Compliance Mapping
| Requirement | Control in TrustBrain™ |
|---|---|
| NIST AI RMF — GOVERN | Governor agent = policy authority; SoD Worker/Governor |
| NIST AI RMF — MEASURE | Blast-radius score, audit ledger, integrity attestation |
| NIST AI RMF — MANAGE | HITL thresholds, reversibility contract, rollback |
| EU AI Act Art. 12 (record-keeping) | Cryptographic SHA-256 audit ledger |
| EU AI Act Art. 14 (human oversight) | HITL queue + decider identity on resolve |
| ISO 27001 A.12/A.16 | Config baselines, drift events, incident-response playbooks |

---
*Prepared by Nedo (CEO) — nTrust.ai. "It's the numbers we trust."*
