"""Connectors Control 19: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.19",
    family="connectors",
    title='Connectors Control 19',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="classify",
    configuration={'field': 'owner', 'target': 'connectors_value_19'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
