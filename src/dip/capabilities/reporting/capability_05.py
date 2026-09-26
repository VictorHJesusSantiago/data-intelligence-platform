"""Reporting Control 05: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.05",
    family="reporting",
    title='Reporting Control 05',
    description='Operational reports, delivery schedules and export preparation',
    operation="aggregate",
    configuration={'field': 'source', 'target': 'reporting_value_05'},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
