"""Dbms Control 26: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.26",
    family="dbms",
    title='Dbms Control 26',
    description='Relational storage, indexing, query and transaction operations',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'dbms_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
