"""Etl Control 03: Extract, transform and load processing steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="etl.03",
    family="etl",
    title='Etl Control 03',
    description='Extract, transform and load processing steps',
    operation="project",
    configuration={'field': 'email', 'target': 'etl_value_03', 'fields': ['id', 'email', 'value']},
    tags=("etl", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
