"""Finops Control 17: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.17",
    family="finops",
    title='Finops Control 17',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="dedupe",
    configuration={'field': 'value', 'target': 'finops_value_17'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
