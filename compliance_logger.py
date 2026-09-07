"""
compliance_logger.py — nTrust.ai compliance event logger (NIST AI RMF + EU AI Act).
Standalone CLI / importable module. Mirrors ComplianceLogger in frts_core.py for
non-FRTS events (risk decisions, board approvals, model actions).
"""

import argparse, hashlib, json, sys, uuid
from datetime import datetime, timezone


class ComplianceEventLogger:
    def __init__(self, sink=None):
        self.sink = sink or sys.stdout
        self.events = []

    def log(
        self, entity_id, actor, action, severity="INFO", detail="", human_approval=None
    ):
        ts = datetime.now(timezone.utc).isoformat()
        rec = {
            "event_id": f"EVT-{uuid.uuid4().hex[:10].upper()}",
            "entity_id": entity_id,
            "actor": actor,
            "action": action,
            "severity": severity,
            "detail": detail,
            "human_approval": human_approval,  # HITL chain (EU AI Act Art.14)
            "ts": ts,
        }
        canonical = json.dumps(rec, sort_keys=True, default=str)
        rec["sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        self.events.append(rec)
        self.sink.write(json.dumps(rec) + "\n")
        return rec["event_id"]


def main():
    p = argparse.ArgumentParser(description="nTrust.ai compliance logger")
    p.add_argument("--entity", required=True)
    p.add_argument("--actor", required=True)
    p.add_argument("--action", required=True)
    p.add_argument("--severity", default="INFO")
    p.add_argument("--detail", default="")
    args = p.parse_args()
    logger = ComplianceEventLogger()
    eid = logger.log(args.entity, args.actor, args.action, args.severity, args.detail)
    print(f"logged {eid}")


if __name__ == "__main__":
    main()
