"""Finops Control 12: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.12",
    family="finops",
    title='Finops Control 12',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="filter_not_null",
    configuration={'field': 'owner', 'target': 'finops_value_12'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
