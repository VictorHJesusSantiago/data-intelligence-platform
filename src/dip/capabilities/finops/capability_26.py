"""Finops Control 26: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.26",
    family="finops",
    title='Finops Control 26',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'finops_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
