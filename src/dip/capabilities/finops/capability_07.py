"""Finops Control 07: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.07",
    family="finops",
    title='Finops Control 07',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="dedupe",
    configuration={'field': 'value', 'target': 'finops_value_07'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
