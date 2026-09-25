"""Etl Control 09: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.09",
    family="etl",
    title='Etl Control 09',
    description='Extract, transform and load processing steps',
    operation="classify",
    configuration={'field': 'source', 'target': 'etl_value_09'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
