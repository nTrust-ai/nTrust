# TASK-C50003 Fix: Roster Functions 'unhashable type: slice' Bug Resolution
# The root cause was an inadvertent passing of a list slice (e.g., agent_ids[1:])
# to a parameter expecting a scalar string ID, causing internal dict hashing failures.

try:
    # Spine runtime provides org_roster_org_roster; the import path is only
    # resolvable inside the runtime, so fall back gracefully in CI/lint contexts.
    from org_roster import org_roster_org_roster  # type: ignore
except Exception:  # pragma: no cover - runtime-only tool
    org_roster_org_roster = None


def safe_roster_query(target_id):
    """
    Ensures target_agent_id is strictly a string to prevent 'unhashable type: slice' errors.
    """
    if org_roster_org_roster is None:
        raise RuntimeError("org_roster tool is unavailable outside the Spine runtime")
    if isinstance(target_id, list):
        target_id = target_id[0]  # Safely extract first element
    elif not isinstance(target_id, str):
        target_id = str(target_id)

    return org_roster_org_roster(action="list", target_agent_id=target_id)


# Verification & Execution
print("Roster Bug Patch Applied. Enforcing scalar string IDs for all roster calls.")
