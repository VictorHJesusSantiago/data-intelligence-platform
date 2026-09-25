"""Dbms Control 14: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.14",
    family="dbms",
    title='Dbms Control 14',
    description='Relational storage, indexing, query and transaction operations',
    operation="derive",
    configuration={'field': 'region', 'target': 'dbms_value_14', 'factor': 1.14},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
