"""Dbms Control 19: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.19",
    family="dbms",
    title='Dbms Control 19',
    description='Relational storage, indexing, query and transaction operations',
    operation="classify",
    configuration={'field': 'status', 'target': 'dbms_value_19'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
