"""Reporting Control 08: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.08",
    family="reporting",
    title='Reporting Control 08',
    description='Operational reports, delivery schedules and export preparation',
    operation="mask",
    configuration={'field': 'region', 'target': 'reporting_value_08'},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
