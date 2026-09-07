"""
nTrust Shield - Database Schema Initialization
MVP Support for SQLite/PostgreSQL
Phase 1: Production Foundation
Date: 2026-06-24
"""

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

Base = declarative_base()


class AuditLog(Base):
    """Structured audit log entry for compliance tracking"""

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    event_type = Column(String(100), nullable=False)
    actor_id = Column(String(100))
    resource_type = Column(String(100))
    resource_id = Column(String(100))
    action = Column(String(100), nullable=False)
    status = Column(String(50), default="completed")
    details = Column(Text)
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)


class SecurityEvent(Base):
    """Security-related events for threat detection"""

    __tablename__ = "security_events"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    severity = Column(String(20), nullable=False)  # low, medium, high, critical
    event_category = Column(String(100), nullable=False)
    source_ip = Column(String(45))
    target_resource = Column(String(255))
    description = Column(Text, nullable=False)
    resolved = Column(Boolean, default=False)
    resolution_notes = Column(Text)


class SystemConfig(Base):
    """System configuration key-value store"""

    __tablename__ = "system_config"

    id = Column(Integer, primary_key=True)
    config_key = Column(String(255), unique=True, nullable=False)
    config_value = Column(Text)
    description = Column(String(500))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserSession(Base):
    """Active user session tracking for security monitoring"""

    __tablename__ = "user_sessions"

    id = Column(Integer, primary_key=True)
    session_id = Column(String(255), unique=True, nullable=False)
    user_id = Column(String(100))
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)


def init_database(db_url=None):
    """Initialize database with schema"""
    if db_url is None:
        db_url = os.getenv("DATABASE_URL", "sqlite:///ntrust_shield.db")

    engine = create_engine(db_url, echo=False)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create session factory
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return engine, SessionLocal


def get_db_session(SessionLocal):
    """Get database session context manager"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    # Test initialization
    print("Initializing nTrust Shield database schema...")
    engine, SessionLocal = init_database()
    print("✓ Database schema created successfully")
    print(f"✓ Engine: {engine}")

    # Verify tables exist
    from sqlalchemy import inspect

    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f"✓ Tables created: {tables}")
