"""Dbms Control 23: Relational storage, indexing, query and transaction operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="dbms.23",
    family="dbms",
    title='Dbms Control 23',
    description='Relational storage, indexing, query and transaction operations',
    operation="project",
    configuration={'field': 'value', 'target': 'dbms_value_23', 'fields': ['id', 'value', 'value']},
    tags=("dbms", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
