"""Finops Control 24: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.24",
    family="finops",
    title='Finops Control 24',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="derive",
    configuration={'field': 'amount', 'target': 'finops_value_24', 'factor': 1.24},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
