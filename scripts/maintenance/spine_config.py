#!/usr/bin/env python3
import sys
import os
import json

CONFIG_PATH = "/app/data/orgs/org_ntrust/config/spine_config.json"
DEFAULT_CONFIG = {
     "email_smtp": {"host": "smtp.ntrust.ai", "port": 587, "user": "", "password": ""},
     "email_imap": {"host": "imap.ntrust.ai", "port": 993, "user": "", "password": ""},
     "telegram": {"bot_token": "", "chat_ids": []},
     "auto_updates": {"enabled": True, "interval_hours": 24}
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=4)

def list_config():
    config = load_config()
    print("=== SPINE CONFIGURATION PARAMETERS ===")
    for table, params in config.items():
        print(f"\n[{table.upper()}]")
        for key, value in params.items():
            print(f"    {key}: {value}")
    print("\n=====================================")

def update_config(table, key, value):
    config = load_config()
    if table not in config:
        print(f"❌ Error: Table '{table}' not found.")
        sys.exit(1)
    if key not in config[table]:
        print(f"❌ Error: Key '{key}' not found in table '{table}'.")
        sys.exit(1)
    try:
        config[table][key] = json.loads(value)
    except json.JSONDecodeError:
        config[table][key] = value
    save_config(config)
    print(f"✅ Updated {table}.{key} = {config[table][key]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 spine_config.py [list|update] [--table <table> --key <key> --value <value>]")
        sys.exit(1)
    
    action = sys.argv[1]
    if action == "list":
        list_config()
    elif action == "update":
        if len(sys.argv) != 6 or sys.argv[2] != "--table" or sys.argv[4] != "--key":
            print("Usage: python3 spine_config.py update --table <table> --key <key> --value <value>")
            sys.exit(1)
        table = sys.argv[3]
        key = sys.argv[5]
        value = sys.argv[6]
        update_config(table, key, value)
    else:
        print(f"❌ Unknown action: {action}")
        sys.exit(1)
