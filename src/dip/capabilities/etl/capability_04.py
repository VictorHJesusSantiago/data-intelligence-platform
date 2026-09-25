"""Etl Control 04: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.04",
    family="etl",
    title='Etl Control 04',
    description='Extract, transform and load processing steps',
    operation="derive",
    configuration={'field': 'event_time', 'target': 'etl_value_04', 'factor': 1.04},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
