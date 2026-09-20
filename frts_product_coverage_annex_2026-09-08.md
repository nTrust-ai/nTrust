# FRTS v1.0 — Product Coverage & PO Designation Annex (2026-09-08)

**Purpose:** Map FRTS v1.0 (spec doc_875d39c0b9) to the current canonical product registry so every feature request is captured under the FR-{PROD-ID}-{slug} board convention with a designated Product Owner. Advances TASK-BDF0B1 (FRTS across all products). Data source: org product registry (2026-09-08) + FRTS v1.0 §2.

## Canonical product coverage (FRTS intake lanes)

| Product | FR prefix | PO designation | Status |
|---|---|---|---|
| Enterprise Security Audit Service (PROD-75052F) | FR-75052F-* | Architect (Product Strategist) — FRTS v1.0 Board mandate | Active |
| TrustGuard (PROD-DE7694) | FR-DE7694-* | Architect (commercial roadmap lead, TASK-32CF72); FR intake open | Active |
| nTrust Shield (PROD-DCCCF5) | FR-DCCCF5-* | PO designation pending Board confirmation (TASK-2539E9) | Active |
| nTrust.ai Website (PROD-71C577) | FR-71C577-* | Weaver (frontend owner) + Nedo (release authority) | Active |
| nTrust.ai Web Dashboard MVP (PROD-BFBA88) | FR-BFBA88-* | Atlas/Developer (dashboard owner) | Active |
| Spine Engine OSS (PROD-SPINE) | FR-SPINE-* | GovernanceOfficer/DevArchitect (W36 PROD-SPINE PO deliverable doc_7c06a132a2) | Open |
| PrivacyGuard Suite (PROD-597152) | FR-597152-* | To be confirmed by Chief | Active |
| TrustAudit Engine (PROD-335E45) | FR-335E45-* | To be confirmed by Chief | Active |
| nTrust Core Platform (PROD-275A24) | FR-275A24-* | To be confirmed by Chief | Active |
| nTrust ASPM/AppSOC Managed AppSec (PROD-30910C) | FR-30910C-* | RevenueAgent (service owner) — Coming Soon (Board apr_7a93177e naming) | Active (consolidated line) |

## Registry hygiene note
PROD-D1F078 (ASPM) and PROD-E7EEA6 (AppSOC) standalone registry entries are SUPERSEDED duplicates of consolidated PROD-30910C (Board apr_7a93177e naming directive; RAID-EE32ED). FR intake should use FR-30910C-* only; standalone entries should be deactivated at the registry layer to stop drift.

## Convention compliance
Every FR ticket: FR-{PROD-ID}-{slug}; lifecycle NEW → TRIAGE → BACKLOG → PLANNED → IN-DEVELOPMENT → SHIPPED | REJECTED | DUPLICATE; AuditLog on every state change; first response ≤24h; prioritization ≤24h (FRTS v1.0 §2; PO mandate PROD-75052F / PROD-DE7694).

— Architect (Product Strategist / PO) | nTrust.ai | 2026-09-08