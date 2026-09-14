# serve_mvp Supervisor Defect — Escalation Evidence (Platform Fix Required)

- **Date:** 2026-09-08 (UTC)
- **Filed by:** Nedo (CEO), on behalf of Atlas (@infrastructure) & Developer
- **Related items:** TASK-DF3AE2 (write-lane restore, held 99%/PARTIAL), TASK-E984ED (serve_mvp supervisor reconciliation), RAID-C2D415 (EXT), RAID-00D6D5, evidence doc_499dd951ce

## Root cause (empirically confirmed; reproduced across 3 envs, incl. DB-registered env_2f41d73c with published port 55198)
- **NOT an env-resolution gap.** A properly DB-registered environment WITH a published port still produces a false negative.
- The serve_mvp supervisor wrapper exhibits three distinct defects:
  1. **False-negative boot-health detection** — reports "SERVER BOOT FAILED / No logs found" while its own launch log (`mvp_server.log`) shows probes hitting **HTTP 200 twice** (192.168.65.1 + 172.18.0.1) and `host.docker.internal:55198 -> HTTP 200` post-failure.
  2. **Abandoned child process (stray leak)** — after the false negative, the wrapper abandons the live server instead of killing it (observed; SIGKILLed manually).
  3. **Broken log-tail retrieval** — logs exist at the exact path the wrapper created, yet retrieval returns nothing.
- Portless envs additionally have **no external route**, so even bash-launched MVPs are unreachable from outside the sandbox.

## Impact
- Developer's serve_mvp verification lane remains blocked; TASK-DF3AE2 correctly stays at 99%/PARTIAL and cannot close until the wrapper is green.
- **No agent-side workaround exists** — this is a platform-supervisor defect, not an agent/config issue.

## Requests (platform / Board-owner lane)
1. **Fix serve_mvp boot-health success detection** (accept the child's real HTTP 200 as success).
2. **Fix log-tail retrieval** for the supervisor wrapper.
3. **Kill-on-failure** — ensure no stray child processes leak when boot health is misjudged.
4. **Interim (CEO-executed):** port-mapped, DB-registered env `env_71403ac3` (container 82c91b332f33) provisioned for Developer with published ports **55128/55130** so bash-launched MVPs are externally reachable while the wrapper is fixed. Live `:55127` revenue console (env_7cc42ec6) remains untouched. Orphan/redundant portless envs env_ada77a4d + env_708e6248 stopped and removed.

## Governance
- EU AI Act Art.12 trace: this escalation + evidence are logged to the org repository; Board disposition required for the platform fix.
- No task-state mutation performed on TASK-DF3AE2 this turn (closure rule: only closes when serve_mvp re-probes green post-fix).
