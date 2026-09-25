"""Etl Control 07: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.07",
    family="etl",
    title='Etl Control 07',
    description='Extract, transform and load processing steps',
    operation="dedupe",
    configuration={'field': 'status', 'target': 'etl_value_07'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
