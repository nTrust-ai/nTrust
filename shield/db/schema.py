"""
nTrust Shield MVP: Database Schema Initialization
Product: nTrust Shield (Cybersecurity & Privacy Automation)
Owner: Architect (Product Strategist)
Date: 2026-06-24
Status: Working Implementation
"""

import sqlite3
from datetime import datetime
from typing import Optional, List, Dict
import os

# Database path relative to workspace
DB_PATH = os.getenv("SHIELD_DB_PATH", "/app/data/orgs/org_ntrust/shield/data/shield.db")

def init_database() -> None:
    """Initialize the SQLite database with core security tables."""
    # Ensure data directory exists
    data_dir = os.path.dirname(DB_PATH)
    os.makedirs(data_dir, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create 'incidents' table for threat logging
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        severity TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create 'audit_logs' table for compliance tracking
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        action TEXT NOT NULL,
        resource_type TEXT,
        resource_id TEXT,
        ip_address TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL
    )
    """)

    # Create 'users' table for basic access control
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        role TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create 'config' table for system settings
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS config (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Insert default configuration
    default_configs = [
        ("system_name", "nTrust Shield MVP"),
        ("version", "0.1.0"),
        ("security_level", "high"),
        ("audit_enabled", "true")
    ]
    cursor.executemany("INSERT OR IGNORE INTO config (key, value) VALUES (?, ?)", default_configs)

    conn.commit()
    conn.close()
    print(f"✅ Database initialized at {DB_PATH}")

def get_incidents(severity: Optional[str] = None, status: str = "open") -> List[Dict]:
    """Retrieve incidents with optional filtering."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = "SELECT * FROM incidents WHERE 1=1"
    params = []
    
    if severity:
        query += " AND severity = ?"
        params.append(severity)
    
    if status:
        query += " AND status = ?"
        params.append(status)
    
    query += " ORDER BY created_at DESC"
    
    cursor.execute(query, params)
    columns = [desc[0] for desc in cursor.description]
    incidents = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    conn.close()
    return incidents

def log_audit(user_id: str, action: str, resource_type: str, resource_id: str, ip_address: str, status: str) -> None:
    """Log an audit event."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO audit_logs (user_id, action, resource_type, resource_id, ip_address, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, action, resource_type, resource_id, ip_address, status))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    
    # Test log
    log_audit("admin", "init", "system", "shield_db", "127.0.0.1", "success")
    print("✅ Audit log test successful.")