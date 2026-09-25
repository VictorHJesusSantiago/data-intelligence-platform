"""Etl Control 18: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.18",
    family="etl",
    title='Etl Control 18',
    description='Extract, transform and load processing steps',
    operation="mask",
    configuration={'field': 'amount', 'target': 'etl_value_18'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
