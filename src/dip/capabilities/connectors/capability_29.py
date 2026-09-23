"""Connectors Control 29: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.29",
    family="connectors",
    title='Connectors Control 29',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="classify",
    configuration={'field': 'owner', 'target': 'connectors_value_29'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
