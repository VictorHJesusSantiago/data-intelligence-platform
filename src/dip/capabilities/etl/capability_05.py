"""Etl Control 05: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.05",
    family="etl",
    title='Etl Control 05',
    description='Extract, transform and load processing steps',
    operation="aggregate",
    configuration={'field': 'category', 'target': 'etl_value_05'},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
