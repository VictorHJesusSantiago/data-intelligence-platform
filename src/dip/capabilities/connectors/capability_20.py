"""Connectors Control 20: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.20",
    family="connectors",
    title='Connectors Control 20',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="timestamp",
    configuration={'field': 'status', 'target': 'connectors_value_20'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
