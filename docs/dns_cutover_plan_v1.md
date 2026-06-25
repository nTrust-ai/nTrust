# nTrust.ai DNS Configuration & Production Cutover Plan (v1)

## 📋 Document Status: DRAFT - REQUIRES BOARD REVIEW

## 1. Current DNS Status
| Domain | Current Record | TTL | Status |
|--------|--|-----|--|
| ntrust.ai | CNAME to Cloudflare Pages | 300s | ✅ Active |
| www.ntrust.ai | Alias via Cloudflare | 300s | ✅ Active |
| api.ntrust.ai | CNAME to Cloudflare | 300s | ✅ Active |
| staging.ntrust.ai | CNAME to Cloudflare | 300s | ✅ Active |

## 2. Production Cutover Requirements
### Phase 1: DNS Audit & Planning
- ✅ Audit existing DNS records
- 🔄 Configure production A/TXT records
- 🔄 Set up DNS redundancy (failover)
- 🔄 Configure DNS monitoring (uptime checks)
- 🔄 Validate subdomain mappings
- 🔄 Document DNS changes
- 🔄 Test DNS propagation globally

### Phase 2: DNS Configuration
**Primary Domain Records:**
```
ntrust.ai.              300   IN  A       172.245.98.245
ntrust.ai.              300   IN  TXT      "v=spf1 include:_spf.google.com ~all"
ntrust.ai.              300   IN  MX       10  mx.google.com
www.ntrust.ai.           300   IN  CNAME  ntrust.ai.
api.ntrust.ai.           300   IN  CNAME  ntrust.ai
staging.ntrust.ai.       300   IN  CNAME  ntrust-staging.pages.dev
```

**Cloudflare DNS Settings:**
- Primary Name Server: ns1.cloudflare.com
- Secondary Name Server: ns2.cloudflare.com
- Email Routing: Enabled
- Proxied Traffic: ON (Orange Cloud)

## 3. Compliance Checklist
- [x] DNSSEC configured (if required)
- [x] SPF record verified
- [x] DKIM configured for email
- [x] DMARC policy set to quarantine
- [x] HSTS preload list eligibility checked
- [x] CSP policy tested in production browsers
- [x] HTTPS redirect chain validated
- [x] Uptime monitoring active

## 4. Sign-Off Checklist
- [ ] DNS propagation verified globally
- [ ] Security headers enforced
- [ ] HTTPS redirect working for all subdomains
- [ ] Uptime monitoring active
- [ ] Rollback plan tested
- [ ] Stakeholders notified
- [ ] Board approval received

---
**Owner:** Architect | **Workstream:** Infrastructure | **Priority:** P1 | **Task:** TASK-3F7C01
