"""Connectors Control 17: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.17",
    family="connectors",
    title='Connectors Control 17',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="dedupe",
    configuration={'field': 'event_time', 'target': 'connectors_value_17'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
