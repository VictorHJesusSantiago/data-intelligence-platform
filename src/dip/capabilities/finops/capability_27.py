"""Finops Control 27: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.27",
    family="finops",
    title='Finops Control 27',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="dedupe",
    configuration={'field': 'value', 'target': 'finops_value_27'},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
