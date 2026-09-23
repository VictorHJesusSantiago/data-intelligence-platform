"""Connectors Control 16: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.16",
    family="connectors",
    title='Connectors Control 16',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'connectors_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
