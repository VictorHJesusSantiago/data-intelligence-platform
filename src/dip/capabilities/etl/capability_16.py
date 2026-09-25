"""Etl Control 16: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.16",
    family="etl",
    title='Etl Control 16',
    description='Extract, transform and load processing steps',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'etl_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
