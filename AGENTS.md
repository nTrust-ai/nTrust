# nTrust.ai Repository Rules & Architecture Guide (AGENTS.md)

This document defines the strict architectural boundaries, operational protocols, and safeguards for all AI agents (Nedo, Weaver, Developer, Atlas, Architect, SRE) operating in the `ntrustai/nTrust` repository.

---

## 🏛️ 1. Repository Identity & Production Hosting Architecture

- **Public Production Presence**: This repository hosts the public production website for **nTrust.ai** (serving `https://ntrust.ai`).
- **Hosting Engine**: Deployed natively via **Cloudflare Pages**, triggered on pushes to the `main` branch.
- **Build Output Directory**: Cloudflare Pages publishes the `dist/` directory.
- **Build Command**: Cloudflare Pages executes `npm run build`, which runs `node build.js`.

---

## 📁 2. Canonical Source of Truth (`frontend/dist/`)

1. **The Definitive Source**: The static multi-page website files live in [`frontend/dist/`](./frontend/dist/).
   - `frontend/dist/index.html` — Canonical homepage (Hero, Products, Spine Platform, Pricing, About/Leadership).
   - `frontend/dist/about.html` — About Us & Leadership profile.
   - `frontend/dist/pricing.html` — Transparent pricing tiers.
   - `frontend/dist/contact.html` — Enterprise contact & inquiry page.
   - `frontend/dist/naveed/index.html` — Executive Biography for Founder & President Naveed Ul Islam.
   - `frontend/dist/products/` — 12 individual product and service solution pages.
   - `frontend/dist/assets/site.css` — Shared design system stylesheet.
   - `frontend/dist/_redirects` — Cloudflare Pages redirects and rewrites.
   - `frontend/dist/_headers` — Production security and CSP headers.
2. **Build Pipeline (`build.js`)**:
   - `build.js` synchronizes all files from `frontend/dist/` into `dist/` and mirrors them into `public/`.
   - `build.js` runs a mandatory 21-endpoint verification gate. If any critical page is missing, empty, or unlinked, the build **fails immediately with exit code 1**.

---

## 🚫 3. Absolute Prohibitions (Never Do This)

1. **NO Single-Page MVP Overwrites**:
   - NEVER overwrite root `index.html` or `dist/index.html` with an MVP dashboard, test portal, or experimental app.
   - The root website MUST remain the full, multi-page corporate marketing presence.
2. **NO Destructive Bundlers (`vite build`)**:
   - NEVER revert `package.json` `"build"` script to `vite build` or any tool that wipes `dist/`.
   - `vite build` assumes a single-page app and clears the directory, which destroys the multi-page suite.
3. **NO Scope Drift / Tunnel Vision**:
   - When asked to update a specific page (e.g., `/naveed` or `/pricing.html`), you MUST NOT delete, rename, or ignore the rest of the site.
   - You MUST test the whole website suite before considering any task complete.
4. **NO Open Source Labeling**:
   - All references to "Open Source" have been retired across navigation, footers, copy, and metadata.
   - Spine is referred to as the **Spine Engine** / **Autonomous AI Architecture**, and all Spine product links must point to `https://spine.ntrust.ai`.

---

## 🛠️ 4. How to Update the Website Safely (Board-Approved Workflow)

When the Board (Naveed Ul Islam) requests an update to the website:

1. **Edit Canonical Files**:
   Make edits only in [`frontend/dist/`](./frontend/dist/) (e.g. `frontend/dist/index.html`, `frontend/dist/naveed/index.html`, `frontend/dist/about.html`).
2. **Execute Build Verification**:
   Run `npm run build` locally. Verify that the build outputs:
   `🎉 [nTrust Build] All 21 critical endpoints verified successfully! Ready for Cloudflare Pages deployment.`
3. **Pre-Push Full Suite Regression Check**:
   Before pushing, verify the critical endpoints locally:
   - Apex homepage (`dist/index.html`) contains the complete multi-page layout.
   - Executive profile (`dist/naveed/index.html`) is intact and links properly.
   - Stylesheet (`dist/assets/site.css`) is present and populated.
   - Redirects (`dist/_redirects`) contain all active rules.
4. **Atomic Git Push**:
   Commit with a clear, conventional commit message (`feat(site): ...` or `fix(site): ...`) and push to `main`.
5. **Post-Deploy Live Probe**:
   Probe live endpoints:
   - `curl -sIL https://ntrust.ai/` $\rightarrow$ HTTP 200
   - `curl -sIL https://ntrust.ai/naveed` $\rightarrow$ HTTP 200
   - `curl -sIL https://ntrust.ai/about.html` $\rightarrow$ HTTP 200
   - `curl -sIL https://ntrust.ai/pricing.html` $\rightarrow$ HTTP 200
   - `curl -sIL https://ntrust.ai/contact.html` $\rightarrow$ HTTP 200

---

## 🚀 5. Where MVP Code Belongs

- Autonomous products (TrustGuard, PrivacyGuard, TrustAudit) are functional software applications.
- MVP code must reside in designated directories (e.g., `src/trustguard/`, `mvp/`, or distinct product repos/submodules).
- MVP testing must run on dedicated staging ports or subdomains (e.g., `trustguard.ntrust.ai` or internal Docker sandboxes), **NEVER** replacing the apex marketing website at `https://ntrust.ai/`.
