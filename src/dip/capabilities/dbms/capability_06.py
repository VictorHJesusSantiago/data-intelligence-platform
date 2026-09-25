"""Dbms Control 06: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.06",
    family="dbms",
    title='Dbms Control 06',
    description='Relational storage, indexing, query and transaction operations',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'dbms_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
