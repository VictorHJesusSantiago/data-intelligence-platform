"""Olap Control 29: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.29",
    family="olap",
    title='Olap Control 29',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="classify",
    configuration={'field': 'region', 'target': 'olap_value_29'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
