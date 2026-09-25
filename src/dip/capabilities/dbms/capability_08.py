"""Dbms Control 08: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.08",
    family="dbms",
    title='Dbms Control 08',
    description='Relational storage, indexing, query and transaction operations',
    operation="mask",
    configuration={'field': 'owner', 'target': 'dbms_value_08'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
