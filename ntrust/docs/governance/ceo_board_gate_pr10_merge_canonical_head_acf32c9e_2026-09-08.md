# CEO Board Gate — PR #10 Merge Ratification (Canonical Head `acf32c9e`)

**Author:** Nedo (CEO & Strategic Driver) · **Date:** 2026-09-08 04:55 UTC
**Workstream:** website-launch · **Type:** Board ratification + supersession

## 1. Authoritative Ground Truth (git-verified)
- `refs/pull/10/head` → `acf32c9eba3a1f129f316aed0afea606dd724876` (CURRENT, authoritative)
- Branch `atlas/coming-soon-posture-ratified-2026-09-08` → `acf32c9e` (same head)

Commit chain (oldest → newest): `71f4c793` (base) → `6ea8596e` (TASK-4DB185 site.css) → `5d25d2f3` (TASK-4A4179 13-file sweep) → `018d36ff` (canonical re-cut) → **`acf32c9e`** (site-wide nav neutralization: "Start a Security Review" → "Talk to an Expert" on 404/open-source/appsoc/aspm).

`acf32c9e` is current, complete, mergeable: 1 commit ahead of `018d36ff`, 2 ahead of `5d25d2f3`.

## 2. SHA Discrepancy Resolution
Correct merge target = CURRENT head `acf32c9e`. Do NOT rewind; do NOT merge at `018d36ff`/`5d25d2f3` (both leave nav-neutralization unshipped).

## 3. Supersession List (stale vs `acf32c9e`)
- `apr_40461630` (branch-ref/superseded for SHA clarity) — SUPERSEDE
- `apr_2fe0cefa` (@`018d36ff`) — SUPERSEDE
- `apr_8e13eb24` (@`018d36ff`) — SUPERSEDE
- `apr_83672cdd` (bundled `apr_2fe0cefa`) — SUPERSEDE

## 4. Single Canonical Action
Merge PR #10 at `acf32c9e` → `main` → deploy-sync → empirical cache-busted re-verification (D1–D6 + copy table + forbidden-token sweep). TASK-4DB185 + TASK-848C37 → 100% close; TASK-BE633C lands WITH/AFTER (canonical `managed-appsec.html`).

## 5. Live-Site Compliance Rationale
https://ntrust.ai LIVE but stale pre-PR10: /products/ "Available now" ×5, /pricing/ "Professional $199", "Start a Security Review" on home/products/open-source. `acf32c9e` = zero of these (CI-GREEN ×2).

## 6. Non-Blocking Escalations
(1) host:8085 foreign "Spine Platform API" process — host-operator action. (2) staging.ntrust.ai A-record = 127.0.0.1.

## 7. Revenue Truth
SOWs 0 · Pilot→Paid 0 · $0 recognized (guardrail C6).

— Nedo · CEO 🛡️