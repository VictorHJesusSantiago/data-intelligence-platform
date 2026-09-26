"""Reporting Control 12: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.12",
    family="reporting",
    title='Reporting Control 12',
    description='Operational reports, delivery schedules and export preparation',
    operation="filter_not_null",
    configuration={'field': 'owner', 'target': 'reporting_value_12'},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
