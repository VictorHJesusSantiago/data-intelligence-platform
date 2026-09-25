"""Etl Control 25: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.25",
    family="etl",
    title='Etl Control 25',
    description='Extract, transform and load processing steps',
    operation="aggregate",
    configuration={'field': 'category', 'target': 'etl_value_25'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
