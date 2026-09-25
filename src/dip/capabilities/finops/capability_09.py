"""Finops Control 09: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.09",
    family="finops",
    title='Finops Control 09',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="classify",
    configuration={'field': 'email', 'target': 'finops_value_09'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
