"""Etl Control 22: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.22",
    family="etl",
    title='Etl Control 22',
    description='Extract, transform and load processing steps',
    operation="filter_not_null",
    configuration={'field': 'region', 'target': 'etl_value_22'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
