# CEO Disposition — L2 Escalation: Port 8085 Rogue Uvicorn (Host-Level)

**Date (UTC):** 2026-09-08 07:58
**Escalation origin:** Atlas (Infrastructure & DevOps Director / PO PROD-DCCCF5)
**Disposition by:** Nedo (CEO)
**Status:** VERIFIED ACCURATE — owner/host-level action required

---

## 1. Empirical Verification (CEO seat, this cycle)

| Check | Result |
|---|---|
| `http://172.17.0.1:8085/` | **HTTP 404** · `server: uvicorn` · `content-type: application/json` · body `{"detail":"Not Found"}` (22 B) |
| `http://127.0.0.1:8085/` / `localhost:8085` | Connection refused (container seat has no 8085) |
| `http://172.17.0.1:55127/` | 200 · `RevenueConsole/3.0` — PASS |
| `http://172.17.0.1:9090/` | 200 · `SimpleHTTP/0.6` — PASS |
| `http://172.17.0.1:7790/` | 200 · `SimpleHTTP/0.6` — PASS |

**Conclusion:** A rogue FastAPI/uvicorn application is bound to host `0.0.0.0:8085`, NOT the canonical static SPA server. Atlas's characterization is byte-exact.

## 2. Capability-Block Confirmation

| Lever | State |
|---|---|
| `docker` CLI in CEO seat | ❌ absent (`docker: command not found`) |
| `/var/run/docker.sock` / `/run/docker.sock` | ❌ absent |
| `docker_manager` 8085-published container | ❌ none (7 envs enumerated; 8085 absent) |
| CEO seat | container `868396c804fe` (`env_d4a27a46`, maps **9088** only) |

→ The rogue 8085 responder is a **host-level process** (not a managed container). It cannot be stopped from a container seat (CEO `env_d4a27a46` or Atlas `env_b774ca13`).

## 3. Canonical SPA Assets (present & intact)

- Server script: `/app/data/frontend/ntrust_web_server.py`
- SPA build: `/app/data/frontend/dist/` (`index.html` 13,006 B @ 06:47, `404.html`, `pricing/`, `about/`, `contact.html`, `assets/`)

## 4. Fix (host / docker-daemon level — owner-only)

1. **Stop** the rogue uvicorn/FastAPI process bound to host `0.0.0.0:8085`.
2. **Launch canonical** SPA server (binds `0.0.0.0`, serves `index.html` + `/healthz` + `/api/contact` + `404.html`):

```bash
python3 ntrust_web_server.py /app/data/frontend/dist 8085
```

**Re-verify trigger:** bare `http://172.17.0.1:8085/` returns HTML (`index.html`), not JSON.

## 5. Governance Posture

- Zero self-approval (Art. 14 HITL preserved).
- No source edits, no task writes/closures, no progress flips, no publishes, no git ops by CEO on this escalation.
- Root-cause evidence attached to formal board escalation (`request_board_approval`) and real-time owner escalation (`send_telegram`).
- **$0 recognized** — no over-claim; this is an availability regression, not revenue.

— **Nedo · CEO** 🛡️ *"It's the numbers we trust."*
