"""Data Quality Control 02: Profiling, validation, remediation and quality scoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_quality.02",
    family="data_quality",
    title='Data Quality Control 02',
    description='Profiling, validation, remediation and quality scoring',
    operation="filter_not_null",
    configuration={'field': 'status', 'target': 'data_quality_value_02'},
    tags=("data_quality", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
