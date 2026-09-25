"""Dbms Control 30: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.30",
    family="dbms",
    title='Dbms Control 30',
    description='Relational storage, indexing, query and transaction operations',
    operation="timestamp",
    configuration={'field': 'amount', 'target': 'dbms_value_30'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
