from pydantic import BaseModel, Field
from enum import Enum


class Severity(str, Enum):
    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"


class VulnerabilityReport(BaseModel):
    asset_id: str
    severity: Severity
    description: str
    remediation: str = ""
