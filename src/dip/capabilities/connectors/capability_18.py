"""Connectors Control 18: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.18",
    family="connectors",
    title='Connectors Control 18',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="mask",
    configuration={'field': 'category', 'target': 'connectors_value_18'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
