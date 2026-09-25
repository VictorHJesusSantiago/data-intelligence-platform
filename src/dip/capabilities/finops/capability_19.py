"""Finops Control 19: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.19",
    family="finops",
    title='Finops Control 19',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="classify",
    configuration={'field': 'email', 'target': 'finops_value_19'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
