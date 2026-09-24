"""Data Quality Control 03: Profiling, validation, remediation and quality scoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_quality.03",
    family="data_quality",
    title='Data Quality Control 03',
    description='Profiling, validation, remediation and quality scoring',
    operation="project",
    configuration={'field': 'amount', 'target': 'data_quality_value_03', 'fields': ['id', 'amount', 'value']},
    tags=("data_quality", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
