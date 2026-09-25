"""Etl Control 21: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.21",
    family="etl",
    title='Etl Control 21',
    description='Extract, transform and load processing steps',
    operation="profile",
    configuration={'field': 'value', 'target': 'etl_value_21'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
