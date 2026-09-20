#!/usr/bin/env python3
"""nTrust Spine Configuration Manager — Phase 3 Production Readiness"""
import json, os, sys, argparse

CONFIG_DIR = "/app/data/orgs/org_ntrust/.config"
CONFIG_FILE = os.path.join(CONFIG_DIR, "params.json")

DEFAULT_PARAMS = {
    "email_smtp": {"value": "smtp.ntrust.ai", "port": 587, "enabled": True},
    "email_imap": {"value": "imap.ntrust.ai", "port": 993, "enabled": True},
    "telegram_alerts": {"enabled": True, "chat_id": "", "bot_token": ""},
    "auto_updates": {"enabled": True, "interval_hours": 24},
    "compliance_logging": {"enabled": True, "log_path": "/app/data/orgs/org_ntrust/audit_log.json"},
    "production_server": {"port": 8085, "bind": "0.0.0.0", "docroot": "/app/data/orgs/org_ntrust/dashboard"},
    "trustguard_port": {"port": 55130, "bind": "0.0.0.0"},
    "service_catalog_port": {"port": 9090, "bind": "0.0.0.0"}
}

def ensure_config():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_PARAMS, f, indent=2)
    return CONFIG_FILE

def list_params(table=None):
    config = ensure_config()
    with open(config) as f:
        params = json.load(f)
    if table:
        if table in params:
            print(f"=== {table.upper()} ===")
            for k, v in params[table].items():
                print(f"  {k}: {v}")
        else:
            print(f"Table '{table}' not found. Available: {list(params.keys())}")
    else:
        for table_name, items in params.items():
            print(f"\n=== {table_name.upper()} ===")
            for k, v in items.items():
                print(f"  {k}: {v}")

def update_param(table, key, value):
    config = ensure_config()
    with open(config) as f:
        params = json.load(f)
    if table not in params:
        print(f"Table '{table}' not found. Available: {list(params.keys())}")
        sys.exit(1)
    params[table][key] = value
    with open(config, 'w') as f:
        json.dump(params, f, indent=2)
    print(f"✅ Updated {table}.{key} = {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="nTrust Spine Configuration Manager")
    subparsers = parser.add_subparsers(dest="command")
    
    list_parser = subparsers.add_parser("list", help="List all configuration parameters")
    list_parser.add_argument("--table", help="Filter by specific table")
    
    update_parser = subparsers.add_parser("update", help="Update a configuration parameter")
    update_parser.add_argument("--table", required=True, help="Configuration table name")
    update_parser.add_argument("--key", required=True, help="Parameter key")
    update_parser.add_argument("--value", required=True, help="New value")
    
    args = parser.parse_args()
    
    if args.command == "list":
        list_params(args.table)
    elif args.command == "update":
        update_param(args.table, args.key, args.value)
    else:
        list_params()
