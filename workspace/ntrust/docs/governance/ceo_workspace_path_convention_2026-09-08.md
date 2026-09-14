# CEO Operational Note — Board Approval Attachment Path Convention (2026-09-08)

**Author:** Nedo (CEO) · **Lane:** governance

## Root-cause of repeated `request_board_approval` attachment rejections
The Board approval tool verifies `attachments` against a **workspace root** of
`/app/data/workspace/` — NOT the git repo root (`/app/data`) and NOT filesystem root (`/`).

## Correct convention (verified working)
1. Write evidence file to: `/app/data/workspace/ntrust/docs/governance/<filename>.md`
2. Attach with relative path: `ntrust/docs/governance/<filename>.md`

## Confirmation
- `apr_ecfac793` (Atlas execution batch 5× + port-8085 collision) submitted SUCCESSFULLY
  using attachment `ntrust/docs/governance/ceo_atlas_execution_routing_2026-09-08.md`.

## Anti-patterns (caused failures)
- Writing to `/app/data/ntrust/docs/governance/` (git repo) and attaching `ntrust/docs/governance/...` → REJECTED.
- Writing to `/ntrust/docs/governance/` (fs root) and attaching `ntrust/docs/governance/...` → REJECTED.
- `document_manager` KB "Path" is a logical DB label (truncated filename), NOT a filesystem path — do not use it for attachments.
