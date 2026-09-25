"""Dbms Control 27: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.27",
    family="dbms",
    title='Dbms Control 27',
    description='Relational storage, indexing, query and transaction operations',
    operation="dedupe",
    configuration={'field': 'category', 'target': 'dbms_value_27'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
