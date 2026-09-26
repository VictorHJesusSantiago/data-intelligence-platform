"""Reporting Control 09: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.09",
    family="reporting",
    title='Reporting Control 09',
    description='Operational reports, delivery schedules and export preparation',
    operation="classify",
    configuration={'field': 'email', 'target': 'reporting_value_09'},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
