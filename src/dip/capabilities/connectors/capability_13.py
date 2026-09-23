"""Connectors Control 13: Reusable interfaces for databases, files, APIs and message systems."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="connectors.13",
    family="connectors",
    title='Connectors Control 13',
    description='Reusable interfaces for databases, files, APIs and message systems',
    operation="project",
    configuration={'field': 'id', 'target': 'connectors_value_13', 'fields': ['id', 'id', 'value']},
    tags=("connectors", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
