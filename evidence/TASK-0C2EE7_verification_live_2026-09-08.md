# TASK-0C2EE7 (PROD-71C577) — Live Verification Record (Atlas, 2026-09-08)
GitHub repo + Cloudflare Pages verification for the nTrust.ai public site / Part-B pricing posture.

## Raw evidence (direct reads)
1) git remote -v -> origin = https://github.com/ntrustai/nTrust.git
2) git rev-parse origin/main (post-fetch) -> 4709dd9cc24d229f6ecfa0d5882edef00e29814c
3) git merge-base --is-ancestor 9985cd4e origin/main -> YES
   9985cd4e = "Merge PR #10: Coming-Soon posture + site-wide nav neutralization (canonical head acf32c9e) — Board apr_95116a9a APPROVED"
4) grep frontend/dist/pricing.html @ main: "coming soon"=3, "start a security review"=0, "no purchase required today." present
5) Live Cloudflare Pages apex (urllib, HTTP):
   https://ntrust.ai/pricing.html          -> 200, 6993B; coming soon x3; "start a security review" x0; "no purchase required today" x1; buy/checkout x0
   https://ntrust.ai/                       -> 200; coming soon x10; "start a security review" x0
   https://ntrust.ai/products/appsoc.html   -> 200; coming soon x4; "start a security review" x0
   https://ntrust.ai/404.html               -> 200; talk-to-an-expert x1; order/buy x0

## Result
Repo configured + Cloudflare Pages serving merged PR #10 content with Part-B pricing posture (Coming Soon + de-purchase, zero order-intent CTAs). Verification GREEN.
