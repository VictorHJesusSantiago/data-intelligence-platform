"""Reporting Control 03: Operational reports, delivery schedules and export preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="reporting.03",
    family="reporting",
    title='Reporting Control 03',
    description='Operational reports, delivery schedules and export preparation',
    operation="project",
    configuration={'field': 'status', 'target': 'reporting_value_03', 'fields': ['id', 'status', 'value']},
    tags=("reporting", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
