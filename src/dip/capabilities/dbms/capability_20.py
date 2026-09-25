"""Dbms Control 20: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.20",
    family="dbms",
    title='Dbms Control 20',
    description='Relational storage, indexing, query and transaction operations',
    operation="timestamp",
    configuration={'field': 'amount', 'target': 'dbms_value_20'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
