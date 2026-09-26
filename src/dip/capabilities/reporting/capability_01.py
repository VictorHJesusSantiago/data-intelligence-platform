"""Reporting Control 01: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.01",
    family="reporting",
    title='Reporting Control 01',
    description='Operational reports, delivery schedules and export preparation',
    operation="profile",
    configuration={'field': 'category', 'target': 'reporting_value_01'},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
