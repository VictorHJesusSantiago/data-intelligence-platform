"""Etl Control 20: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.20",
    family="etl",
    title='Etl Control 20',
    description='Extract, transform and load processing steps',
    operation="timestamp",
    configuration={'field': 'id', 'target': 'etl_value_20'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
