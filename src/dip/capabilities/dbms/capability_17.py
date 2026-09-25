"""Dbms Control 17: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.17",
    family="dbms",
    title='Dbms Control 17',
    description='Relational storage, indexing, query and transaction operations',
    operation="dedupe",
    configuration={'field': 'category', 'target': 'dbms_value_17'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
