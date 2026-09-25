"""Finops Control 01: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.01",
    family="finops",
    title='Finops Control 01',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="profile",
    configuration={'field': 'category', 'target': 'finops_value_01'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
