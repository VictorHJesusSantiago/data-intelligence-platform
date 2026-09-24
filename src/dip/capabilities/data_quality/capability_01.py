"""Data Quality Control 01: Profiling, validation, remediation and quality scoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_quality.01",
    family="data_quality",
    title='Data Quality Control 01',
    description='Profiling, validation, remediation and quality scoring',
    operation="profile",
    configuration={'field': 'owner', 'target': 'data_quality_value_01'},
    tags=("data_quality", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
