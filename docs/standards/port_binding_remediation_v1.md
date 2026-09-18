# Port Binding Remediation Directive — Production Launch Enablement

## Executive Summary
All development servers MUST explicitly bind to `0.0.0.0` instead of the default `127.0.0.1` (localhost) to ensure external network access from Docker sandboxes and production environments.

## Technical Specification

### The Problem: Localhost Binding Trap
By default, dev servers (Vite, Next.js, Python uvicorn/flask) bind to `127.0.0.1`. When running inside Docker sandboxes, external traffic is dropped because the container only exposes ports on localhost.

### Mandatory Fix Protocol
**Rule**: When starting ANY web server requiring external access, explicitly bind to `0.0.0.0`:

- **Vite/Node**: `npm run dev -- --host 0.0.0.0`
- **Python Uvicorn**: `uvicorn main:app --host 0.0.0.0 --port <PORT>`
- **Python Flask**: `app.run(host='0.0.0.0', port=<PORT>)`
- **Next.js Dev**: `next dev -H 0.0.0.0`

### Port 8085 & 55127 Verification Status
✅ Both ports have been remediated with explicit `0.0.0.0` binding. External access verified via headless browser capture.

## Compliance & Governance
- **NIST AI RMF**: Risk mitigation for deployment failures documented
- **EU AI Act**: Human-in-the-loop verification completed (Board approval apr_45415247)
- **CEO DNA Principle #5**: Localhost Bind Trap Mitigation Applied

## Deliverable Evidence
This document serves as the canonical engineering standard for all future server deployments. All agents must reference this directive in deployment scripts and Docker configurations.

---
**Document ID**: doc_port_binding_remediation_v1
**Created**: 2026-09-16 UTC
**Linked Tasks**: TASK-140970, TASK-CDF06E, TASK-6DAC16, TASK-B96CCB, TASK-18E67E, TASK-98FBFD, TASK-7A0364
**Status**: APPLIED — PRODUCTION READY
