"""Dbms Control 16: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.16",
    family="dbms",
    title='Dbms Control 16',
    description='Relational storage, indexing, query and transaction operations',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'dbms_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
