"""Reporting Control 07: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.07",
    family="reporting",
    title='Reporting Control 07',
    description='Operational reports, delivery schedules and export preparation',
    operation="dedupe",
    configuration={'field': 'value', 'target': 'reporting_value_07'},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
