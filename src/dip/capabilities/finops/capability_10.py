"""Finops Control 10: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.10",
    family="finops",
    title='Finops Control 10',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="timestamp",
    configuration={'field': 'event_time', 'target': 'finops_value_10'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
