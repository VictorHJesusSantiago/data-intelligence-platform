"""Dbms Control 07: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.07",
    family="dbms",
    title='Dbms Control 07',
    description='Relational storage, indexing, query and transaction operations',
    operation="dedupe",
    configuration={'field': 'category', 'target': 'dbms_value_07'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
