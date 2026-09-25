"""Finops Control 25: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.25",
    family="finops",
    title='Finops Control 25',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="aggregate",
    configuration={'field': 'source', 'target': 'finops_value_25'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
