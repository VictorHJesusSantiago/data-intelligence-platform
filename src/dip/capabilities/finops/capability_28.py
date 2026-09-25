"""Finops Control 28: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.28",
    family="finops",
    title='Finops Control 28',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="mask",
    configuration={'field': 'region', 'target': 'finops_value_28'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
