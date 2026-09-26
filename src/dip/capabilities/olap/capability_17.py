"""Olap Control 17: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.17",
    family="olap",
    title='Olap Control 17',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="dedupe",
    configuration={'field': 'id', 'target': 'olap_value_17'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
