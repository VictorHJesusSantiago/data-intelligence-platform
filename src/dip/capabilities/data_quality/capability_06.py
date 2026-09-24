"""Data Quality Control 06: Profiling, validation, remediation and quality scoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_quality.06",
    family="data_quality",
    title='Data Quality Control 06',
    description='Profiling, validation, remediation and quality scoring',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_quality_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("data_quality", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
