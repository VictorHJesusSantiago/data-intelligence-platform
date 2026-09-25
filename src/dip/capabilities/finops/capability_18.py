"""Finops Control 18: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.18",
    family="finops",
    title='Finops Control 18',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="mask",
    configuration={'field': 'region', 'target': 'finops_value_18'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
