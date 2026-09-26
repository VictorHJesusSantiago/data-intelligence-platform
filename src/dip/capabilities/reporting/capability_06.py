"""Reporting Control 06: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.06",
    family="reporting",
    title='Reporting Control 06',
    description='Operational reports, delivery schedules and export preparation',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'reporting_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
