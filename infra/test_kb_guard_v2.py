#!/usr/bin/env python3
"""
test_kb_guard_v2.py — Regression suite for TASK-27E190.

Proves the corrected KB fragmentation guard (v2) does NOT false-positive on
the 12 documented incidents, while STILL catching a genuine same-category
duplicate (so the guard remains effective, just not over-broad).
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kb_fragmentation_guard_v2 import (  # noqa: E402
    DocRegistryEntry,
    KbFragmentationGuardV2,
    DEDUPE_IMMUNE_CATEGORIES,
)

PASS, FAIL = 0, 0


def check(name: str, cond: bool, detail: str = ""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}  {detail}")


def registry_guard(entries):
    return KbFragmentationGuardV2(registry=entries)


def main() -> int:
    print("KB guard v2 regression suite (TASK-27E190)")
    print("=" * 56)

    # ---- Fixture: governance/evidence records with sibling revisions -------
    gov_sib1 = DocRegistryEntry("doc_94b752e5bf", "Spine Engine OSS One-Pager v2", "evidence")
    gov_sib2 = DocRegistryEntry("doc_038f80b53e", "Spine Engine OSS One-Pager v2 (rev)", "evidence")
    dec_a = DocRegistryEntry("doc_21977174c6", "CEO Decision Record 2026-09-08", "decision")
    dec_b = DocRegistryEntry("doc_6845d5b432", "CEO Decision Record 2026-09-08 (Architect disposition)", "decision")
    memo1 = DocRegistryEntry("doc_8dc1e2d0a7", "Chief Decision Memo v4", "governance")
    cat = DocRegistryEntry("doc_dea46bbd13", "TrustGuard Service Catalog v1.4", "catalog")
    orphan = DocRegistryEntry("doc_2e482a2b1d", "orphan registry ref", "governance",
                              disk_path="__missing_on_disk__.md")

    g = registry_guard([gov_sib1, gov_sib2, dec_a, dec_b, memo1, cat, orphan])
    g.reconcile()

    # ---- 1. Reconciliation quarantines phantom entry ------------------------
    check("phantom quarantine removes doc_2e482a2b1d",
          "doc_2e482a2b1d" in g.quarantined_phantoms)

    # ---- 2. Evidence siblings are NOT flagged as fragments (v1 would) -------
    flag, reason = g.is_duplicate_fragment(gov_sib2)
    check("evidence sibling NOT flagged", flag is False, reason)
    # v1 demonstrably false-positived here:
    flag1, _ = g.is_duplicate_fragment_v1(gov_sib2)
    check("(v1 legacy WOULD have flagged — defect confirmed)", flag1 is True)

    # ---- 3. Decision / governance records NOT flagged -----------------------
    for e in (dec_b, memo1):
        flag, reason = g.is_duplicate_fragment(e)
        check(f"{e.category} record NOT flagged ({e.doc_id})", flag is False, reason)

    # ---- 4. Same-title governance record with SAME blob -> genuine dup ------
    dec_dup = DocRegistryEntry("doc_XXXXdeadbeef", dec_a.title, "decision",
                               blob_sha="abc123")
    dec_a.blob_sha = "abc123"
    g2 = registry_guard([dec_a, dec_dup])
    flag, reason = g2.is_duplicate_fragment(dec_dup)
    check("true exact duplicate still flagged", flag is True, reason)

    # ---- 5. Same-category high-similarity content doc -> genuine flag -------
    prod1 = DocRegistryEntry("doc_a1111111", "TrustGuard Pricing Page v3 (final)", "catalog")
    prod2 = DocRegistryEntry("doc_a2222222", "TrustGuard Pricing Page v3 (final draft)", "catalog")
    g3 = registry_guard([prod1])
    flag, reason = g3.is_duplicate_fragment(prod2)
    check("same-category catalog near-duplicate flagged (effective)", flag is True, reason)

    # ---- 6. Cross-category collision NOT flagged ----------------------------
    prod3 = DocRegistryEntry("doc_a3333333", "Enterprise Security Audit SOW", "product")
    prod4 = DocRegistryEntry("doc_a4444444", "Enterprise Security Audit SOW (record)", "evidence")
    g4 = registry_guard([prod3])
    flag, reason = g4.is_duplicate_fragment(prod4)
    check("cross-category collision NOT flagged", flag is False, reason)

    # ---- 7. Dedupe-immune set sanity -----------------------------------------
    check("governance/evidence/audit/closure/decision all immune",
          {"governance", "evidence", "audit", "closure", "decision"} <= DEDUPE_IMMUNE_CATEGORIES)

    print("=" * 56)
    print(f"RESULT: {PASS} passed, {FAIL} failed")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
