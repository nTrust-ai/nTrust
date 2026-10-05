# TrustGuard — durable static route

Permanent, non-rotating surface for the TrustGuard product.

- Landing:  `/trustguard/`
- Health:   `/trustguard/health.json`  (machine-checkable compliance posture)
- Demo ops: `/trustguard/dashboard.html`

## Design
- **Pure static** — no server process to keep alive. Once deployed to Cloudflare
  Pages it is durable by construction and independent of any agent sandbox.
- **Self-contained** — inline CSS, no third-party JS, no external fetches except
  the same-origin `health.json`.
- **Sanitized** — customer-facing copy only; no internal designators, ticket IDs
  or build codes.

## Uptime evidence
`.github/workflows/trustguard-uptime.yml` probes this surface from GitHub-hosted
runners (out of sandbox) every 15 minutes and appends results to
`evidence/uptime/`. The `>=24h sustained external 200s` bar is met when
`evidence/uptime/trustguard_uptime_summary.json` reports
`meets_24h_bar: true`.
