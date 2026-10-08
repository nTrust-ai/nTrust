# 🚀 Vercel Deployment Request — TrustBrain™ Portal (trustbrain.ntrust.ai)

**Status**: `READY FOR HUMAN WORKER CONNECTION`
**Scaffold Author**: Atlas (Infrastructure & DevOps Director)
**Date**: 2026-10-07

## 📦 Repository Handoff Details
For the human worker to connect this repository to Vercel and provision `trustbrain.ntrust.ai`:

### 1. GitHub Repository Link
```text
https://github.com/ntrustai/trustbrain-app
```

### 2. Framework Preset Selection
In Vercel Dashboard, select: **Next.js** (or static HTML/React depending on the scaffolded structure).

### 3. Required Environment Variables (Keys Only)
No plaintext secrets are present in this repository. The human worker must provision these keys in the Vercel dashboard `Settings > Environment Variables`:
- `NEXT_PUBLIC_APP_NAME` = "TrustBrain Licensing Portal"
- `NEXT_PUBLIC_PRODUCT_ID` = "PROD-TB01"
- `NEXT_PUBLIC_API_BASE_URL` = (To be configured post-deploy)

### 4. Build & Output Directory
- **Build Command**: Default (or `npm run build` if using a framework)
- **Output Directory**: `out` or `.next` (depending on scaffold type)
- **Install Command**: `npm install`

### 5. Post-Deployment Verification Checklist
- [ ] Confirm `trustbrain.ntrust.ai` resolves and serves the TrustBrain Landing Page (Pillar 3).
- [ ] Verify the Licensing Portal entry point (Pillar 2) is accessible at root or `/portal`.
- [ ] Ensure no internal sprint codes, MVP tags, or "Phase 1/2/3" labels are visible to external users.

---
**Action Required**: Human worker to link repo `ntrustai/trustbrain-app` in Vercel, apply the above presets, and confirm live DNS propagation for `trustbrain.ntrust.ai`.
