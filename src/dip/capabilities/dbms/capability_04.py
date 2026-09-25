"""Dbms Control 04: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.04",
    family="dbms",
    title='Dbms Control 04',
    description='Relational storage, indexing, query and transaction operations',
    operation="derive",
    configuration={'field': 'region', 'target': 'dbms_value_04', 'factor': 1.04},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
