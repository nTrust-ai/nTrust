# User Onboarding Flowchart Specification (v1.0)
**Workstream**: TrustGuard Pilot | **Phase**: 1 Closure Deliverable
**Date**: 2026-06-04 | **Author**: Product Strategist (Architect)

## 1. Executive Summary
This specification details the step-by-step user onboarding flowchart for the TrustGuard MVP dashboard. It is designed to minimize drop-off, enforce security baselines early, and guide users toward their First Value Action (FVA) within the first session. This artifact directly supports TASK-ED3143 closure and feeds into Phase 2 UI/UX development.

## 2. Flowchart Sequence & Decision Nodes
### Step 1: Registration & Authentication Gate
- **Action**: User enters email/password or SSO provider.
- **Validation**: Email format check + password strength meter (min 10 chars, special char required).
- **Decision Node**: Valid credentials? -> Proceed to verification. Invalid -> Show inline error & retry.
- **Output**: Verification email dispatched. Account placed in `pending_verification` state.

### Step 2: Email Verification & TOS Acceptance
- **Action**: User clicks unique magic link or enters 6-digit code.
- **Validation**: Token expiry check (15 min window).
- **Decision Node**: Verified? -> Redirect to Dashboard Setup. Expired/Invalid -> Prompt resend.
- **Output**: Account status updated to `active_unconfigured`.

### Step 3: Primary Configuration Wizard
- **Action**: Guided UI flow presenting mandatory setup steps.
- **Steps**: 
   1. Select pilot tier (Starter/Pro/Enterprise)
   2. Configure default security policies (CSP, HSTS preload toggle)
   3. Add initial target domains/endpoints
- **Validation**: At least one target domain must be added to proceed.
- **Output**: Dashboard UI populated with user's tenant context.

### Step 4: First Value Action (FVA) Trigger
- **Action**: "Run Initial Scan" or "Upload Sample Config" prompt appears prominently.
- **Validation**: System checks for pending targets. If none, redirects back to Step 3.
- **Decision Node**: FVA completed? -> Mark user as `activated`. Timeout (72h)? -> Send automated reminder email.
- **Output**: User enters active pilot cohort. Telemetry events logged.

### Step 5: Post-Onboarding Feedback Loop
- **Action**: Micro-survey modal appears post-FVA.
- **Fields**: NPS score, feature usability rating, pain point selection.
- **Validation**: Submission required to unlock advanced dashboard features.
- **Output**: Data routed to centralized feedback queue for product team review.

## 3. Edge Cases & Error Handling
- **Broken Verification Link**: Auto-revocation + secure re-generation flow.
- **Session Timeout**: Grace period (5 min) before forced logout. Local storage preserved if possible.
- **Tenant Isolation Failure**: Immediate lockdown, alert to admin, and manual audit trigger.

## 4. Design & Engineering Handoff Notes
- All flowchart steps must be implemented with progressive enhancement principles.
- Mobile responsiveness required for Steps 1-2; desktop optimized for Steps 3-5.
- Analytics events tagged with `onboarding_step_X` for funnel conversion tracking.
- UI/UX team to translate this spec into Figma wireframes for Phase 2 design sprint.

---
*End of Document v1.0 | Authored for TASK-ED3143 Closure*
