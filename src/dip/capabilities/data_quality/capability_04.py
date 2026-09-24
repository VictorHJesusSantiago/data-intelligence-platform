"""Data Quality Control 04: Profiling, validation, remediation and quality scoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_quality.04",
    family="data_quality",
    title='Data Quality Control 04',
    description='Profiling, validation, remediation and quality scoring',
    operation="derive",
    configuration={'field': 'source', 'target': 'data_quality_value_04', 'factor': 1.04},
    tags=("data_quality", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
