"""Finops Control 02: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.02",
    family="finops",
    title='Finops Control 02',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="filter_not_null",
    configuration={'field': 'owner', 'target': 'finops_value_02'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
