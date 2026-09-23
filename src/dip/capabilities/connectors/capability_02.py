"""Connectors Control 02: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.02",
    family="connectors",
    title='Connectors Control 02',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="filter_not_null",
    configuration={'field': 'source', 'target': 'connectors_value_02'},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
