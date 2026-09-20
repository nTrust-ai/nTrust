#!/usr/bin/env python3
"""
Spine Configuration CLI for Phase 3 Infrastructure Management.
Manages Email SMTP/IMAP, Telegram, Auto-Updates, and other system parameters.
Compliant with nTrust.ai Zero-Trust & Radical Transparency mandates.
"""
import sys
import os
import json
import logging

CONFIG_DIR = "/app/data/orgs/org_ntrust/.config"
CONFIG_FILE = os.path.join(CONFIG_DIR, "params.json")
LOG_FILE = os.path.join(CONFIG_DIR, "config_audit.log")

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ensure_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
        logging.info(f"Created config directory: {CONFIG_DIR}")
    if not os.path.exists(CONFIG_FILE):
        defaults = {
             "email_smtp_host": "smtp.ntrust.ai",
             "email_smtp_port": 587,
             "email_imap_host": "imap.ntrust.ai",
             "email_imap_port": 993,
             "telegram_bot_token": "",
             "auto_updates_enabled": True,
             "nist_compliance_mode": True,
             "eu_ai_act_logging": True
         }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(defaults, f, indent=2)
        logging.info("Initialized default configuration parameters.")

def list_config():
    ensure_config()
    try:
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f)
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error reading config: {e}", file=sys.stderr)
        sys.exit(1)

def update_config(table, key, value):
    ensure_config()
    try:
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f)
        if table in data and isinstance(data[table], dict):
            data[table][key] = value
        elif key in data:
            data[key] = value
        else:
            if table not in data:
                data[table] = {}
            data[table][key] = value
        with open(CONFIG_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        logging.info(f"Updated {table}.{key} to {value}")
        print(f"Successfully updated {table}.{key} -> {value}")
    except Exception as e:
        print(f"Error updating config: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: spine_config.py [list|update]")
        print("  list                   - View all configurable parameters")
        print("  update --table <t> --key <k> --value <v> - Update parameter")
        sys.exit(0)
        
    action = sys.argv[1]
    if action == "list":
        list_config()
    elif action == "update":
        args = sys.argv[2:]
        params = {}
        i = 0
        while i < len(args):
            if args[i].startswith('--'):
                key = args[i][2:]
                if i + 1 < len(args):
                    params[key] = args[i+1]
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        if 'table' in params and 'key' in params and 'value' in params:
            update_config(params['table'], params['key'], params['value'])
        else:
            print("Usage: spine_config.py update --table <table> --key <key> --value <value>")
            sys.exit(1)
    else:
        print(f"Unknown action: {action}. Use 'list' or 'update'.")
        sys.exit(1)
