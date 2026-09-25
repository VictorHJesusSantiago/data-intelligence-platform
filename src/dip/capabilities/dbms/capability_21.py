"""Dbms Control 21: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.21",
    family="dbms",
    title='Dbms Control 21',
    description='Relational storage, indexing, query and transaction operations',
    operation="profile",
    configuration={'field': 'source', 'target': 'dbms_value_21'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
