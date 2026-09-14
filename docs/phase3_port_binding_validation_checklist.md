# Phase 3 Infrastructure Remediation & Port Binding Validation Checklist

## Objective
Validate and enforce correct port binding for all Phase 3 services, ensuring external reachability and eliminating port collisions.

## Pre-Flight Validation
- [ ] Verify all dev/prod servers bind to `0.0.0.0` (never `127.0.0.1` only).
- [ ] Confirm no duplicate listeners on critical ports (:8085, :55127, :55198).
- [ ] Check Docker network mode (`host` vs `bridge`) and port mapping consistency.

## Remediation Actions (Pending Board Approval)
1. **Idle Env Teardown**: Stop confirmed-IDLE container `env_2f41d73c` (:55198) to reclaim compute resources.
2. **:8085 Collision Fix**: 
   - Identify & stop stray "Spine Platform API" (FastAPI) process/container.
   - Restart canonical corporate-site server bound explicitly to `0.0.0.0:8085`.
3. **Verification**: Run TCP connectivity checks against all bound services from external endpoint.

## Compliance Alignment
- Aligns with Localhost Bind Trap Protocol (§3 ENGINEERING VELOCITY).
- Supports P1 Phase 3 commercialization readiness (TASK-ABE83C).
- Evidence package ready for Board review upon execution completion.

---
*Prepared by: Atlas, Infrastructure & DevOps Director*