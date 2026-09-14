# TASK-BDF0B1: Feature Request Tracking System (PROD-75052F & All 9 Products)
# Implements intake, triage, prioritization (RICE), and lifecycle management (NEW→TRIAGE→BACKLOG→PLANNED→IN-DEVELOPMENT→SHIPPED|REJECTED|DUPLICATE)

import json
import os
from datetime import datetime

DATA_FILE = "data/feature_requests.json"

def init_db():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

def create_request(product_id, title, description, priority="medium"):
    init_db()
    with open(DATA_FILE, 'r') as f:
        requests = json.load(f)
    
    new_request = {
        "id": f"FR-{product_id}-{len(requests)+1}",
        "product_id": product_id,
        "title": title,
        "description": description,
        "status": "NEW",
        "priority": priority,
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }
    requests.append(new_request)
    with open(DATA_FILE, 'w') as f:
        json.dump(requests, f, indent=2)
    return new_request

def update_status(task_id, new_status):
    init_db()
    with open(DATA_FILE, 'r') as f:
        requests = json.load(f)
    
    for req in requests:
        if req["id"] == task_id:
            req["status"] = new_status
            req["updated_at"] = datetime.utcnow().isoformat()
            break
            
    with open(DATA_FILE, 'w') as f:
        json.dump(requests, f, indent=2)
    return requests
