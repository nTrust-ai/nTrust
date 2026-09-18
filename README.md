# nTrust.ai — Enterprise AI Security Platform

## Overview
nTrust.ai delivers cutting-edge AI security strategy, risk modeling, and compliance automation to protect enterprise assets.

## Product Portfolio
- **PROD-597152** — PrivacyGuard Suite
- **PROD-71C577** — nTrust.ai Website (this repository)
- **PROD-DE7694** — TrustGuard
- **PROD-BFBA88** — nTrust.ai Dashboard

## Development

### Local Development
```bash
npm install
npm run dev        # Starts dev server on http://0.0.0.0:5173
npm run build      # Production build to dist/
npm run preview    # Preview production build locally
```

### Deployment
This project is configured for **Cloudflare Pages** deployment:
- CI/CD pipeline in `.github/workflows/ci.yml`
- Cloudflare Pages config in `wrangler.toml`
- Automatic deployment on push to `main` branch

## Security
- Zero-trust architecture principles
- NIST AI RMF compliance aligned
- CSP headers enforced via Cloudflare Edge Rules

## Contact
For sales inquiries: naveedulislam@gmail.com

---
© 2026 nTrust.ai — "It's the numbers we trust"
