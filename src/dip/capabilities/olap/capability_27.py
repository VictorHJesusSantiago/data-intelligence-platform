"""Olap Control 27: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.27",
    family="olap",
    title='Olap Control 27',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="dedupe",
    configuration={'field': 'id', 'target': 'olap_value_27'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
