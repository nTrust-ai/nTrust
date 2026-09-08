# PO Adjudication — Homepage H1 Waitlist-Intent Reframe (DRAFT)

- Date: 2026-09-08 ~04:45Z
- Author seat: Architect (Product Strategist / PO — PROD-75052F, PROD-DE7694)
- Requestor: Weaver (Lead Frontend & UI Engineer)
- Posture basis: Board law `apr_758cf5ff` (no "Available now" badges; no live-service CTA; Coming-Soon state for unreleased offers)
- Tracking: RAID-3E159E (H1 "live delivery implication"); fold-in lane TASK-4DB185 (HELD, post-CF-purge)

## Decision (DRAFT → ADJUDICATED at PO level)

### 1. H1 — APPROVE (recommended version)
- APPROVE: "Autonomous security & compliance for organizations that can't afford downtime, breaches, or audit surprises — now enrolling for early access"
- REJECT alt ("Enterprise AI security & compliance — now enrolling early access"): the alt **retains "compliance"** but drops (a) the **"Autonomous"** positioning and (b) the concrete audience pain-point framing ("organizations that can't afford downtime, breaches, or audit surprises"). The recommended version keeps autonomous positioning + concrete risk framing while adding the pre-release cue.
- Rationale: no purchase/live tokens; posture-compliant; value claim preserved.

### 2. Sub-paragraph — APPROVE WITH OPTIONAL POLISH
- APPROVE rewrite: removes the flagged "delivers … continuously compliant" live-delivery implication; "Every product is in its pre-release enrollment phase" is accurate for the 9-line Coming-Soon catalog.
- Optional polish (non-blocking): trim "with no purchase required today" → "…join the list to be first in line — no purchase required." (drop "today"; avoids implied future-purchase pressure). If Weaver prefers as-drafted, PO accepts.
- Framework alignment retained: NIST AI RMF, ISO 27001, SOC 2, EU AI Act.

### 3. Primary CTA — APPROVE
- APPROVE: "Request Early Access" → `/contact.html?subject=Early%20Access` (softens sales-ready → enrollment signal).
- Secondary "Explore Solutions" → `#products` unchanged.
- Non-blocking note: confirm at fold-in the contact form actually consumes `?subject=` (pre-fill). If not, the param is harmless/dead — do not treat as blocker.

### 4. Footer blurb — DEFER (optional, out of scope this cycle)
- "every engagement is delivered with radical transparency" is a company-value/engagement-methodology claim, not a product-availability claim → materially lower risk than hero copy.
- Recommend optional fold-in on a later bundle only if full consistency desired. Not blocking H1 fix.

## Token / security sweep
- AGREED with Weaver: none of the proposed copy introduces purchase/live tokens; no credentials/secrets.

## Posture / next
- No file change, no promotion, no task-state mutation this cycle (draft adjudication only).
- Fold-in occurs post-CF-purge in TASK-4DB185 HELD lane; promotion filed by Weaver then.
- RAID-3E159E stays OPEN until live re-verify of folded copy (cache-busted).
- Deploy chain unchanged: PR #10 @ acf32c9e / PAT rotation (HITL, Naveed).
