"""Finops Control 21: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.21",
    family="finops",
    title='Finops Control 21',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="profile",
    configuration={'field': 'category', 'target': 'finops_value_21'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
