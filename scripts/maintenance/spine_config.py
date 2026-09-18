#!/usr/bin/env python3
"""Spine Configuration Manager — System Optimizer CLI"""
import json, os, sys

CONFIG_PATH = "config/system_params.json"

def list_configs():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            print(json.dumps(json.load(f), indent=2))
    else:
        print("SYSTEM_PARAMS_MISSING")
        print("Creating default scaffold...")
        defaults = {
            "smtp": {"host": "smtp.ntrust.ai", "port": 587, "active": True},
            "telegram": {"bot_token": "TBD_BOARD_CHAT_ID", "chat_id": "", "active": True},
            "auto_updates": {"enabled": True, "interval_hours": 24}
        }
        with open(CONFIG_PATH, 'w') as f:
            json.dump(defaults, f, indent=2)
        print("Scaffold created. Run list again to verify.")

def update_config(table, key, value):
    if not os.path.exists(CONFIG_PATH):
        list_configs()
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
    if table in cfg:
        cfg[table][key] = value
        with open(CONFIG_PATH, 'w') as f:
            json.dump(cfg, f, indent=2)
        print(f"Updated {table}.{key} to {value}")
    else:
        print(f"Table '{table}' not found in config. Available: {list(cfg.keys())}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "list":
        print("Usage: python3 scripts/maintenance/spine_config.py list")
        print("Update: python3 scripts/maintenance/spine_config.py update --table <t> --key <k> --value <v>")
    else:
        list_configs()
