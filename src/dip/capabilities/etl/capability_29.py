"""Etl Control 29: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.29",
    family="etl",
    title='Etl Control 29',
    description='Extract, transform and load processing steps',
    operation="classify",
    configuration={'field': 'source', 'target': 'etl_value_29'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
