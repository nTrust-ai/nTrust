**TRUSTGUARD MVP: INFRASTRUCTURE SPEC & BUDGET (PHASE 1)**

**1. TECHNICAL ARCHITECTURE (THE STACK)**
*   **Scan Engine:** Go (Gin Framework) — Native concurrency for high-throughput discovery.
*   **Vector Database:** Milvus — GPU-accelerated indexing for LLM context retrieval.
*   **Graph Database:** Neo4j — High-performance dependency mapping & relationship traversal.
*   **AI Model:** Llama-3 (8B-Quantized) — Running locally on dedicated GPU for zero-latency threat analysis.
*   **Protocol:** Strict mTLS (Zero-Trust) ingress.

**2. FINANCIAL SPECIFICATION (TASK-732D78)**
*Constraint: MVP requires dedicated GPU for Llama-3 inference; CPU-only fails performance targets.*

| Component | Spec | Role | Est. Monthly OpEx |
| :--- | :--- | :--- | :--- |
| **GPU Compute** | 1x AWS `g5.xlarge` (A10G GPU) | Vector Search & LLM Inference | **$700** |
| **App Compute** | 2x AWS `c6i.2xlarge` | Scan Engine / API Core | **$550** |
| **Data Layer** | 1x AWS `r7g.2xlarge` (96GB RAM) | Neo4j & Milvus Persistence | **$550** |
| **Overhead** | VPC / ALB / 500GB NVMe | Networking & Storage | **$150** |
| **TOTAL MOAN** | | | **$1,950** |

**3. ROI & BREAK-EVEN**
*   **Target Price:** $3,000/mo (Enterprise Tier).
*   **Break-Even:** **2 Clients.** (Revenue $6k vs OpEx $1.95k).
*   **Net Margin:** **67%** per client immediately at scale.

**4. MVP ROADMAP PIVOT**
*   **Phase 1 Complete:** Budget & Spec Lock.
*   **Phase 2 (Next):** AWS Provisioning & Core Agent Coding.

**Status:** Awaiting final sign-off to begin provisioning.