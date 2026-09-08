---
title: "CEO DNS Evidence — TASK-8A5E75 spine.ntrust.ai CNAME (Board/Cloudflare-admin action)"
author: "Nedo"
worker_id: "nedo"
created_at: "2026-09-08T07:06:00"
category: "governance"
workstream: "website-launch"
doc_type: "evidence"
version: 1
tags: [dns, spine, task-8a5e75, cloudflare, evidence, ceo]
---

# CEO DNS Evidence — TASK-8A5E75 (spine.ntrust.ai CNAME record)

**Date:** 2026-09-08 07:06 UTC · **Reviewer:** Nedo (CEO, Tier-3) · **Method:** public-DNS resolution probe (Docker resolver, no /etc/hosts override present)

## Empirical DNS state (2026-09-08 07:06 UTC)
| Host | Resolves to | Interpretation |
|---|---|---|
| ntrust.ai | 172.67.211.81 | Cloudflare ✅ (production live) |
| www.ntrust.ai | 172.67.211.81 | Cloudflare ✅ |
| spine.ntrust.ai | **216.198.79.1** | ⚠️ Legacy/non-Cloudflare IP — PROD-SPINE Spec 1 CNAME to Cloudflare NOT yet applied |
| staging.ntrust.ai | 127.0.0.1 | Placeholder/decommissioned state (cutover staging→production) |

## Disposition
- TASK-8A5E75 requires a **Board/Cloudflare-admin action** (create spine.ntrust.ai CNAME). Per Board directive apr_847d85d1 + apr_53aefd5d (2026-09-07): spine.ntrust.ai = Customer Portal (Board-developed/Board-managed); **no agent-lane DNS/Cloudflare/portal mutations**.
- Empirical result confirms the action is **NOT yet executed** (spine.ntrust.ai still resolves to 216.198.79.1). Task state 99% is accurate — remaining 1% is human Board/Cloudflare-admin execution by Naveed.
- No agent-side resolution attempted (EU AI Act Art.14 HITL; DNS mutation guard). No new duplicate task (RAID-B063F2).

— Nedo (CEO) · nTrust.ai · 2026-09-08 07:06 UTC
