#!/usr/bin/env python3
import sys

CONFIG_TABLES = {
    "email": {"smtp_host": "smtp.ntrust.ai", "smtp_port": 587, "imap_host": "imap.ntrust.ai", "imap_port": 993},
    "telegram": {"bot_token": "PLACEHOLDER_TOKEN", "chat_id": "PLACEHOLDER_CHAT"},
    "auto_updates": {"enabled": True, "interval_hours": 24, "rollback_on_fail": True}
}

def list_config():
    for table, params in CONFIG_TABLES.items():
        print(f"\n[Table: {table}]")
        for k, v in params.items():
            print(f"  {k} = {v}")

def update_config(table, key, value):
    if table in CONFIG_TABLES and key in CONFIG_TABLES[table]:
        CONFIG_TABLES[table][key] = value
        print(f"✅ Updated {table}.{key} to '{value}'")
    else:
        print("❌ Invalid table or key.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "list":
        list_config()
    elif args[0] == "update" and "--table" in args:
        try:
            t_idx = args.index("--table")
            k_idx = args.index("--key")
            v_idx = args.index("--value")
            update_config(args[t_idx+1], args[k_idx+1], args[v_idx+1])
        except ValueError:
            print("❌ Usage: spine_config.py update --table <t> --key <k> --value <v>")
