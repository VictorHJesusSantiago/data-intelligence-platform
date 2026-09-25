"""Dbms Control 25: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.25",
    family="dbms",
    title='Dbms Control 25',
    description='Relational storage, indexing, query and transaction operations',
    operation="aggregate",
    configuration={'field': 'email', 'target': 'dbms_value_25'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
