# TrustBrain™ — Licensing Portal & Marketing Hub (Pillar 2/3)

Sovereign AI security **reasoning copilot** surface for nTrust.ai.

This repository is the **Pillar 2 (Licensing / Installer Hub)** and **Pillar 3 (Marketing)** surface for
TrustBrain™, deployed to Vercel as a Next.js application at `https://trustbrain.ntrust.ai`.

> The **Pillar 1 core engine** lives in a separate repository (`ntrustai/trustbrain`) — a standalone
> FastAPI + SQLite OCI container (port 8092) with the dual-agent Worker/Governor architecture.

## Routes

| Route | Purpose |
|---|---|
| `/` | Marketing landing (positioning, differentiators, coverage) |
| `/portal` | Licensing portal (tier matrix, pricing, self-service console, installer) |
| `/install.sh` | Idempotent one-line installer (`curl -fsSL .../install.sh \| bash`) |
| `/api/health` | Health probe |
| `/api/tiers` | Tier entitlement matrix (JSON) |
| `/api/license` | Mock license activation (POST) |

## Local development

```bash
npm install
npm run dev        # binds 0.0.0.0:3000
npm run build      # production build
npm run start      # serve production build
```

## Deployment (Vercel)

- **Framework preset:** Next.js
- **Build command:** `npm run build`
- **Output directory:** `.next`
- **Root directory:** `./`

See the Vercel handoff brief for the human worker connection protocol.
