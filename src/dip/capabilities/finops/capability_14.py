"""Finops Control 14: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.14",
    family="finops",
    title='Finops Control 14',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="derive",
    configuration={'field': 'amount', 'target': 'finops_value_14', 'factor': 1.14},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
