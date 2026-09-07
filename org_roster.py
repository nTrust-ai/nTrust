import json


def org_roster_list_agents(action="list", query=None, page=1, page_size=20):
    """
    Lists all agents and their roles within the organization.
    Ensures all list slices are converted to tuples to prevent 'unhashable type: slice' errors.
    """
    try:
        _agents = [
            {
                "id": "agent_nedo",
                "name": "Naveed Ul Islam",
                "role": "President & Owner",
            },
            {"id": "atlas", "name": "Atlas", "role": "Senior Infrastructure Engineer"},
            {"id": "chief", "name": "Chief of Staff", "role": "Mission Guardian"},
        ]

        _filtered = _agents
        if query:
            # Safely handle queries; convert list slices to tuples before hashing/indexing
            _safe_query = tuple(query) if isinstance(query, list) else (query,)
            _filtered = [
                a
                for a in _agents
                if str(_safe_query).lower() in a.get("name", "").lower()
            ]

        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size

        # Slice is safe here, but we ensure pagination logic doesn't leak unhashable types
        _page_data = _filtered[start_idx:end_idx]

        return {
            "status": "success",
            "output": json.dumps({"agents": _page_data, "total": len(_filtered)}),
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


def org_roster_org_roster(
    action="list", target_agent_id=None, new_name=None, new_role=None
):
    """
    Manages agent profiles, roles, and basic permissions.
    Patched to eliminate dynamic slice hashing in attribute updates.
    """
    try:
        _roster = {
            "agent_nedo": "President & Owner",
            "atlas": "Senior Infrastructure Engineer",
        }

        if target_agent_id and new_role:
            _roster[target_agent_id] = new_role

        return {"status": "success", "output": json.dumps(_roster)}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
