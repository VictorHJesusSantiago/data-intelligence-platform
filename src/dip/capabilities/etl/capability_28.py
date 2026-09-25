"""Etl Control 28: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.28",
    family="etl",
    title='Etl Control 28',
    description='Extract, transform and load processing steps',
    operation="mask",
    configuration={'field': 'amount', 'target': 'etl_value_28'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
