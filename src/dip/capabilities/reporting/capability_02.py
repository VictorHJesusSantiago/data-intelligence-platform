"""Reporting Control 02: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.02",
    family="reporting",
    title='Reporting Control 02',
    description='Operational reports, delivery schedules and export preparation',
    operation="filter_not_null",
    configuration={'field': 'owner', 'target': 'reporting_value_02'},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
