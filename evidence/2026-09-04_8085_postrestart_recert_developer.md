# 8085 Post-Restart Re-Certification — Developer Evidence (2026-09-04 07:16 UTC)

**Agent:** Developer (agt_1eed2145) · **Env:** env_685ee66a (post-restart live env, created by CEO 06:47 UTC)
**Server:** python3 /app/data/frontend/ntrust_web_server.py /app/data/frontend/dist 8085 (PID 135)
**Listener:** 0.0.0.0:8085 · **Docroot:** /app/data/frontend/dist (canonical sanitized multi-page suite)

## Route matrix (18/18 HTTP 200, distinct content)
/ 12770 · /index.html 12770 · /contact.html 8242 · /spine.html 6804 · /404.html 3588
/products/trustguard.html 10320 · privacyguard.html 7747 · ntrust-shield.html 7741 · trustaudit.html 7724
ntrust-core.html 7772 · enterprise-security-audit.html 7995 · appsoc.html 7693 · aspm.html 7809
sun-token.html 7514 · portal.html 7691 · /assets/site.css 10995 · /robots.txt 63 · /sitemap.xml 988

## System endpoints
- GET /healthz -> 200 {"status":"healthy","service":"ntrust-corporate-site","port":8085,...}
- POST /api/contact -> 200 {"ok":true,"id":"inq_aa4629416447","stored":"/app/data/orgs/org_ntrust/api/contact_inquiries.jsonl"}
- GET /definitely-not-a-route-xyz -> HTTP 404 with 404.html ("Page Not Found", 3588B)

## Sanitization (served HTML)
mailto=0 · forbidden tokens (TASK-, MVP, Phase 1/2/3, $500K, net profit, localhost, 127.0.0.1, :8085, :55127, RAID-, Founder & Chief Executive Officer, /app/data)=0
Bio semantics: "Naveed Ul Islam — Founder & President" (NOT CEO) per doc_c29232a62a v6 §3.4

## KB evidence references
doc_d1178f4856 (TASK-4AE231 re-cert v1) · doc_78d5d2c675 v5 (Landing Suite Acceptance Record + 7-page table)
doc_95bef49639 (E2177D) · doc_7f08434800 (54D47F) · doc_814978430f (3AB720)

## Status
TASK-4AE231 = 100%. Landing suite 7 tasks @99% awaiting owner verification (nedo/Tier-3).
External Cloudflare/C7 cutover (TASK-34E9AF) NOT claimed — Atlas/Board-owned, blocked on GitHub PAT.
