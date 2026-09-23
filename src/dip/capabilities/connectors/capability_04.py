"""Connectors Control 04: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.04",
    family="connectors",
    title='Connectors Control 04',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="derive",
    configuration={'field': 'value', 'target': 'connectors_value_04', 'factor': 1.04},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
