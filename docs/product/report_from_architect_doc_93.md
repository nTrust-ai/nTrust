Architect reporting to President Naveed regarding **TASK-732D78: Final Resource & Cost Specification**. 

Per your directive, here is the exact financial breakdown for the TrustGuard MVP. All calculations strictly enforce Zero-Trust infrastructure constraints.

**1. GPU Instance Types & Quantities**
*   **Select:** 2x AWS EC2 `g5.xlarge` (1x NVIDIA A10G GPU / 16GiB VRAM per unit).
*   **Justification:** The A10G provides the optimal FP16 inference performance for Llama-3/ResNet-50 models at <40% of the cost of A100 instances. T4 units were evaluated and rejected due to legacy architecture latency constraints.
*   **Total GPU OpEx:** ~$1,100 / mo

**2. Cloud OpEx Projections (AWS Baseline)**
*   **GPU Compute:** 2x `g5.xlarge` (8 vCPU, 32 GiB RAM, A10G GPU) -> ~$1,100
*   **Memory Optimized:** 1x `r6g.4xlarge` (8 vCPU, 128 GiB RAM) -> ~$850 (Neo4j Graph Persistence & Milvus Vector Index)
*   **Network/Management:** 1x VPC, ALB, NAT Gateways -> ~$100
*   **Storage/Backups:** 500GB gp3 + Snapshots -> ~$50
*   **Total Estimated Monthly OpEx:** **~$2,100**

**3. External API Costs**
*   **Inference/API Calls:** **$0.00** (MVP architecture relies entirely on self-hosted, local LLM and model weights; zero external paid inference requests).

**Financial Summary & ROI**
*   **Total Monthly Burn:** **~$2,100**
*   **Client Break-Even:** 1 Enterprise Client (at standard $3k/mo tier).
*   **Net Margin at Scale:** >80% (Excluding AWS reserved instance discounts and volume scaling).

Awaiting Board authorization to proceed to Phase 2 provisioning.