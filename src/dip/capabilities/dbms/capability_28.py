"""Dbms Control 28: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.28",
    family="dbms",
    title='Dbms Control 28',
    description='Relational storage, indexing, query and transaction operations',
    operation="mask",
    configuration={'field': 'owner', 'target': 'dbms_value_28'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
