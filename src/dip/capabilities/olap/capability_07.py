"""Olap Control 07: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.07",
    family="olap",
    title='Olap Control 07',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="dedupe",
    configuration={'field': 'id', 'target': 'olap_value_07'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
