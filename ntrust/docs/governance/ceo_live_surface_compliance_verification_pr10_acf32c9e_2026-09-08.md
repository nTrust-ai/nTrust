# CEO Live-Surface Compliance Verification — PR #10 Merge @ acf32c9e

**Author:** Nedo (CEO & Strategic Driver)
**Timestamp:** 2026-09-08 ~04:35 UTC
**Classification:** Governance / Art.12 traceability + Art.14 HITL routing
**Workstream:** website-launch

---

## 1. Independent live-surface verification (CEO boundary duty)

Per CEO mandate ("verify what the fleet claims"), I captured and read the live apex directly. Result: **the live surface is STALE pre-PR10 and VIOLATES the ratified Coming-Soon posture (apr_758cf5ff).**

### /products/ (screenshot `ed8274fc.png`, vision-read)
- Products rendered with **"Available now"** status: TrustGuard Security Platform, Enterprise Security Audit, PrivacyGuard Suite.
- No "Coming Soon" labels present.
- No pricing tiers shown (no $49/$199/$599).
- Header CTA **"Start a Security Review"** still present.
- No "Talk to an Expert" CTA.

### / (home, screenshot `f6a24520.png`, vision-read)
- Hero: "Autonomous security & compliance for organizations that can't afford downtime…" (legacy pre-posture framing).
- Primary CTA **"Schedule a Security Audit"** + nav CTA **"Start a Security Review"**.
- No "Get Started on GitHub" / "Bring Your Own AI" / "Get a License" tokens.

### Conclusion
Live apex is the **pre-PR10 build**. This matches Atlas's 04:50 UTC empirical finding. The corrective action is singular and unambiguous: **merge PR #10 → main.**

---

## 2. PR #10 head SHA (verified on-disk)

```
git ls-remote origin 'refs/pull/10/head'
acf32c9eba3a1f129f316aed0afea606dd724876  refs/pull/10/head
```

Current mergeable head = **`acf32c9e`** (includes the 4-line nav-neutralization on /open-source, /appsoc, /aspm, /404 — IN-SCOPE of the ratified Coming-Soon posture; do NOT rewind).

---

## 3. Single canonical ratification directive (no duplicate gates)

**APPROVE** `apr_8e13eb24` → merge PR #10 at **current head `acf32c9e`** (not `018d36ff`).

**REJECT** stale SHA duplicates (double-land prevention RAID-469EA9/1808C5):
- `apr_2fe0cefa` (head `018d36ff`, 2 commits behind)
- `apr_40461630` (head `5d25d2f3`, failed 13/13 gate)

**Already resolved:** `apr_code_cb36a8fd` (REJECTED "route to ceo").

---

## 4. Separately tracked host blockers (NOT part of this click)

1. **host:8085** — occupied by a foreign "Spine Platform API" (FastAPI, non-spine-managed). Customer SPA cannot bind until host operator frees/remaps. Same class as RAID-5A70E1.
2. **staging.ntrust.ai** — A-record = `127.0.0.1` (loopback). Root cause of all "staging unreachable" reports. Requires Cloudflare/DNS-owner correction to a public origin.

---

## 5. Posture

No self-merge. No self-approval of Board-gated mutations. All task/approval mutations remain held pending Naveed's one-click. Revenue truth unchanged: SOWs 0 · Pilot→Paid 0 · $0 recognized (guardrail C6).

— Nedo · CEO 🛡️
