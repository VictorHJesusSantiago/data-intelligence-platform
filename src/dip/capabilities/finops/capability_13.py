"""Finops Control 13: Workload metering, consumption grouping and cost optimization signals."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="finops.13",
    family="finops",
    title='Finops Control 13',
    description='Workload metering, consumption grouping and cost optimization signals',
    operation="project",
    configuration={'field': 'status', 'target': 'finops_value_13', 'fields': ['id', 'status', 'value']},
    tags=("finops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
