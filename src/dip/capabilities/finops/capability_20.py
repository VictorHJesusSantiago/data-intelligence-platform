"""Finops Control 20: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.20",
    family="finops",
    title='Finops Control 20',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="timestamp",
    configuration={'field': 'event_time', 'target': 'finops_value_20'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
