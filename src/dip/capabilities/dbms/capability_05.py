"""Dbms Control 05: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.05",
    family="dbms",
    title='Dbms Control 05',
    description='Relational storage, indexing, query and transaction operations',
    operation="aggregate",
    configuration={'field': 'email', 'target': 'dbms_value_05'},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
