"""Reporting Control 04: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.04",
    family="reporting",
    title='Reporting Control 04',
    description='Operational reports, delivery schedules and export preparation',
    operation="derive",
    configuration={'field': 'amount', 'target': 'reporting_value_04', 'factor': 1.04},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
