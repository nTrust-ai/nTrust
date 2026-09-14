# CEO Review Gate — Weaver 5× P1 Code Promotions: Staged-State Verification Certificate

**Date:** 2026-09-08 ~06:5x UTC
**CEO:** Nedo — zero-trust verification of Weaver's authorization request
**Status:** VERIFIED — staged state matches promotion descriptions; discharge gate submitted to Owner lane

## 1. Approval queue (direct per-ID read — all PENDING at Board)
| Approval | Task | Subject | Board State |
|---|---|---|---|
| apr_code_a943e802 | TASK-BE633C | ASPM/AppSOC single Managed AppSec identity (title/canonical/noindex) | PENDING |
| apr_code_c7dade59 | TASK-AFF2AB | _headers /assets/* short max-age + must-revalidate (no immutable/SWR) | PENDING |
| apr_code_1339b27d | TASK-4DB185 (HELD) | Hero FINAL-LOCK waitlist copy fold-in (index.html) | PENDING |
| apr_code_26a19657 | TASK-709DD8 | /pricing/ card flex-column vertical rhythm (×3) | PENDING |
| apr_code_5b59d6a9 | TASK-4DB185 (root cause) | CSS edge-cache root-cause: /assets/* no immutable on unversioned path | PENDING |

## 2. Empirical verification — canonical /app/data/frontend/dist (this seat, direct read)
- **index.html (hero):** kicker "Early access — now enrolling" ×1 · sub "…no purchase required. Join the list…" (no "today") · CTA-1 "Join the Waitlist" → /contact.html?subject=Early%20Access · CTA-2 "Explore Solutions" → /products/. Single residual "today" sits in the separate plans-transparency sec-sub (line 87) — OUTSIDE hero scope; benign.
- **pricing/index.html:** flex-direction:column ×3 · margin-top:auto ×3 (Starter/Growth/Enterprise bottom-anchored CTAs).
- **_headers:** /assets/* → `Cache-Control: public, max-age=3600, must-revalidate` — NO immutable, NO stale-while-revalidate; root /* max-age=0, must-revalidate. Matches root-cause fix.
- **products/aspm.html + appsoc.html:** single <title> "nTrust ASPM/AppSOC — Managed AppSec Services | nTrust.ai" · canonical → https://ntrust.ai/products/managed-appsec.html · robots noindex,follow. managed-appsec.html = index,follow, canonical self.

## 3. GitHub merge vehicles (API read)
- PR #11 (site.css 8751c9f6 sync) — OPEN on ntrustai/nTrust
- PR #12 (/pricing/ TASK-709DD8 presentation-only) — OPEN on ntrustai/nTrust

## 4. Scope guard / sequencing
Discharge fires ONLY on Naveed's one-click Board gavel (EU AI Act Art.14 HITL preserved — no agent-side merge of the gate). Post-approval sequence (Weaver lane): fetch → apply clean patches → push → merge PR #11/#12 + 3-file hero/headers bundle → apex re-verify → close TASK-4DB185 / AFF2AB / BE633C / 709DD8 to 100%. TASK-0C2EE7 remains Owner-lane (CF Pages connect + DNS cutover).
This gate supersedes the ID list in apr_1b68932d with the authoritative five IDs from the executing lane.

— **Nedo · CEO** · nTrust.ai · "It's the numbers we trust."
