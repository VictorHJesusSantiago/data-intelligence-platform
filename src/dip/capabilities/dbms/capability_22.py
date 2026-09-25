"""Dbms Control 22: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.22",
    family="dbms",
    title='Dbms Control 22',
    description='Relational storage, indexing, query and transaction operations',
    operation="filter_not_null",
    configuration={'field': 'id', 'target': 'dbms_value_22'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
