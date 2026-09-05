# nTrust.ai — Corporate Website (PROD-71C577)

Canonical, sanitized public website for nTrust.ai. Static, dependency-free,
WCAG 2.2 AA, deployable directly to Cloudflare Pages (no build step required).

## Structure

```
index.html       — Home (hero, trust stats, featured services)
services.html    — Service catalog (Live + Coming Soon designations)
pricing.html     — Pricing tiers (SaaS + managed services + consulting)
about.html       — Company, mission, contact
assets/css/      — Design system (tokenized)
assets/js/       — Accessible interactions (no framework)
```

## Content sanitization (enforced)

- No internal development markers (no build/phase/port references).
- Unreleased products are labeled "Coming Soon".
- No credentials, secrets, or internal identifiers on any public surface.

## Cloudflare Pages deployment steps

1. Create a Pages project connected to `github.com/ntrustai/nTrust.git`.
2. Build command: *(none — static site)*. Build output directory: `/` (repo root).
3. Set the production domain to `ntrust.ai` (and `www.ntrust.ai` redirect).
4. Verify HTTP 200 on `/`, `/services`, `/pricing`, `/about` and that all
   internal links resolve (no 404s, no directory listings).

"It's the numbers we trust."
