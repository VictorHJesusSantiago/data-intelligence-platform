"""Finops Control 16: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.16",
    family="finops",
    title='Finops Control 16',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'finops_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
