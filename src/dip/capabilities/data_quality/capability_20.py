"""Data Quality Control 20: Profiling, validation, remediation and quality scoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_quality.20",
    family="data_quality",
    title='Data Quality Control 20',
    description='Profiling, validation, remediation and quality scoring',
    operation="timestamp",
    configuration={'field': 'category', 'target': 'data_quality_value_20'},
    tags=("data_quality", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
