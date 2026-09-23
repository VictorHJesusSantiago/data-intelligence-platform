"""Connectors Control 01: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.01",
    family="connectors",
    title='Connectors Control 01',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="profile",
    configuration={'field': 'amount', 'target': 'connectors_value_01'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
