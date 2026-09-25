"""Dbms Control 10: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.10",
    family="dbms",
    title='Dbms Control 10',
    description='Relational storage, indexing, query and transaction operations',
    operation="timestamp",
    configuration={'field': 'amount', 'target': 'dbms_value_10'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
