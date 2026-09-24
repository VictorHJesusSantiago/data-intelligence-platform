"""Data Quality Control 05: Profiling, validation, remediation and quality scoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_quality.05",
    family="data_quality",
    title='Data Quality Control 05',
    description='Profiling, validation, remediation and quality scoring',
    operation="aggregate",
    configuration={'field': 'id', 'target': 'data_quality_value_05'},
    tags=("data_quality", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
