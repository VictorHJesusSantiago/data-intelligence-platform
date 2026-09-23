"""Connectors Control 25: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.25",
    family="connectors",
    title='Connectors Control 25',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="aggregate",
    configuration={'field': 'region', 'target': 'connectors_value_25'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
