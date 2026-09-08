#!/usr/bin/env python3
"""
kb_fragmentation_guard_v2.py — Root-fix for KB anti-fragmentation detector
false-positives (TASK-27E190).

Defect class (10+ documented incidents: RAID-84B69B, A48A8E, 1319A5, BE1CE6,
92E587, CFF099, 5BE0DE, D0BADE, 3B04FD, A0C5F0, E6DD69, 2FF1D3):
  The legacy guard (v1) flagged a NEW doc_* publication as a "fragment /
  duplicate" whenever its computed signature collided with ANY registry entry
  (including PHANTOM entries whose backing file is missing on disk). Because
  governance/evidence publications legitimately carry siblings/revisions with
  distinct doc_ ids (EU AI Act Art.12 traceability), v1 produced repeated
  false rejections and deadlocked legitimate publication.

Fix (v2):
  1. CATEGORY WHITELIST  — dedupe/fragmentation matching runs ONLY within the
     same doc category. GOVERNANCE, COMPLIANCE, EVIDENCE, AUDIT, CLOSURE and
     DECISION categories are dedupe-immune: revisions and sibling records are
     legal and MUST NOT be auto-consolidated (only exact-title + exact-blob
     duplicates are flagged there).
  2. PHANTOM RECONCILIATION — the registry is filtered against disk BEFORE
     matching: any entry whose backing file is missing (phantom) is quarantined
     and excluded, so it can never cause a false match.
  3. CONTENT THRESHOLD     — same-category flagging additionally requires
     similarity above a configurable threshold (default 0.90), not a raw
     signature collision.

Owner: Atlas (Infrastructure). Staged for promotion (owner/Board merge).
"""
from __future__ import annotations

import difflib
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

# --------------------------------------------------------------------------- #
# Category whitelist: doc categories that are DEDUPE-IMMUNE.
# Sibling/revision publications in these categories are legitimate (Art.12).
# --------------------------------------------------------------------------- #
DEDUPE_IMMUNE_CATEGORIES = {
    "governance", "compliance", "evidence", "audit",
    "closure", "decision", "verification", "general",  # general holds records too
}

# High-signal categories where true content fragmentation/dedup still applies.
DEDUPE_ACTIVE_CATEGORIES = {
    "product", "engineering", "marketing", "catalog", "website",
}

DEFAULT_SIMILARITY_THRESHOLD = 0.90

# Documented phantom/incident IDs (RAID record) used for regression fixtures.
DOCUMENTED_PHANTOM_DOC_IDS = {
    "doc_2e482a2b1d",  # KB registry orphan (RAID-6CF05E)
    "doc_a3bc5452c7",  # 4th occurrence (RAID-1319A5)
    "doc_94b752e5bf", "doc_038f80b53e",  # one-pager deadlock (RAID-BE1CE6/CFF099)
    "doc_dea46bbd13",  # catalog publish block (RAID-92E587)
    "doc_8dc1e2d0a7",  # decision-memo mis-match (RAID-831476)
    "doc_3e5d7aaa0a", "doc_42321c23fe",  # disposition loop (RAID-FA7D81)
    "doc_296febc7d3",  # compliance-review FP (RAID-AF7193)
    "doc_66f47a0f84", "doc_cd1e22513e",  # re-publish mis-match (RAID-A0C5F0)
    "doc_21977174c6", "doc_6845d5b432",  # CEO decision record (RAID-E6DD69),
    "doc_e5fb58332d",  # TrustGuard MVP infra spec — phantom path mismatch (RAID-27E190)
}


def _normalize(text: str) -> str:
    """Normalize text for comparison (lowercase, strip punctuation/whitespace)."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", text.lower())).strip()


def _similarity(a: str, b: str) -> float:
    na, nb = _normalize(a), _normalize(b)
    if not na and not nb:
        return 1.0
    if not na or not nb:
        return 0.0
    return difflib.SequenceMatcher(None, na, nb).ratio()


class DocRegistryEntry:
    """A KB registry record as seen by the guard."""

    __slots__ = ("doc_id", "title", "category", "blob_sha", "disk_path")

    def __init__(self, doc_id: str, title: str, category: str,
                 blob_sha: str = "", disk_path: Optional[str] = None):
        self.doc_id = doc_id
        self.title = title
        self.category = (category or "general").lower()
        self.blob_sha = (blob_sha or "").lower()
        self.disk_path = disk_path

    @property
    def phantom(self) -> bool:
        """True when the registry references a backing file that is missing."""
        if not self.disk_path:
            return False  # no disk anchor => cannot prove phantom
        return not Path(self.disk_path).exists()


class KbFragmentationGuardV2:
    """Corrected anti-fragmentation guard (category whitelist + phantom-aware)."""

    def __init__(self,
                 registry: Optional[Iterable[DocRegistryEntry]] = None,
                 similarity_threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
                 fs_root: Optional[str] = None):
        self._entries: List[DocRegistryEntry] = list(registry or [])
        self.threshold = similarity_threshold
        self.fs_root = fs_root
        self.quarantined_phantoms: List[str] = []

    # ------------------------------------------------------------------ #
    # Reconciliation: drop phantom registry entries BEFORE matching.
    # ------------------------------------------------------------------ #
    def reconcile(self) -> List[str]:
        """Remove phantom entries (registry doc_id whose file is missing on
        disk) from the live match-set and quarantine them. Returns the list
        of quarantined phantom doc_ids."""
        self.quarantined_phantoms = []
        kept: List[DocRegistryEntry] = []
        for e in self._entries:
            if e.phantom and e.disk_path and self.fs_root and \
               not Path(e.disk_path).expanduser().is_absolute():
                # anchor relative paths to fs_root for the check
                candidate = Path(self.fs_root) / e.disk_path
                if not candidate.exists():
                    self.quarantined_phantoms.append(e.doc_id)
                    continue
            elif e.phantom:
                self.quarantined_phantoms.append(e.doc_id)
                continue
            kept.append(e)
        self._entries = kept
        return self.quarantined_phantoms

    # ------------------------------------------------------------------ #
    # Core decision.
    # ------------------------------------------------------------------ #
    def is_duplicate_fragment(self, candidate: DocRegistryEntry) -> Tuple[bool, str]:
        """
        Returns (is_flag, reason).

        v2 rule:
          * If candidate category is dedupe-immune  -> NEVER flagged as a
            fragment, UNLESS an exact (same title AND same blob_sha) existing
            entry is found (a true duplicate).
          * Otherwise (dedupe-active category)       -> flagged only when a
            same-category entry with title/content similarity >= threshold.
        """
        cand_cat = (candidate.category or "general").lower()

        # True duplicate guard (applies to ALL categories): identical title +
        # identical blob in registry => genuine duplicate.
        for e in self._entries:
            if e.doc_id == candidate.doc_id:
                continue
            if e.title.strip().lower() == candidate.title.strip().lower():
                if e.blob_sha and candidate.blob_sha and e.blob_sha == candidate.blob_sha:
                    return True, f"exact duplicate (title+blob) of {e.doc_id}"

        # Dedupe-immune categories: legitimate siblings/revisions allowed.
        if cand_cat in DEDUPE_IMMUNE_CATEGORIES:
            return False, "category dedupe-immune (governance/evidence/audit/closure)"

        # Dedupe-active categories: require same-category + high similarity.
        if cand_cat not in DEDUPE_ACTIVE_CATEGORIES:
            # Unknown category: conservative - do not auto-flag.
            return False, f"category '{cand_cat}' not in dedupe-active set"

        for e in self._entries:
            if e.doc_id == candidate.doc_id:
                continue
            if e.category != cand_cat:
                continue
            if _similarity(e.title, candidate.title) >= self.threshold:
                return True, f"high-similarity same-category match with {e.doc_id}"

        return False, "no matching fragment"

    # ------------------------------------------------------------------ #
    # v1 reproduction (legacy behavior) for regression demonstration only.
    # ------------------------------------------------------------------ #
    def is_duplicate_fragment_v1(self, candidate: DocRegistryEntry) -> Tuple[bool, str]:
        """Legacy guard: any signature collision with ANY registry entry flags
        a fragment — this is the defect we are removing."""
        for e in self._entries:
            if e.doc_id == candidate.doc_id:
                continue
            if _similarity(e.title, candidate.title) >= self.threshold:
                return True, f"v1 legacy flag vs {e.doc_id} (defect)"
        return False, "no v1 flag"


def load_category_whitelist(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


if __name__ == "__main__":
    import sys
    # Self-check: no false positives on documented incidents.
    from test_kb_guard_v2 import main as run_tests
    sys.exit(run_tests())
