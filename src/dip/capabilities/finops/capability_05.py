"""Finops Control 05: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.05",
    family="finops",
    title='Finops Control 05',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="aggregate",
    configuration={'field': 'source', 'target': 'finops_value_05'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
