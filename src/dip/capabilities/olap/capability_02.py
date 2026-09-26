"""Olap Control 02: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.02",
    family="olap",
    title='Olap Control 02',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="filter_not_null",
    configuration={'field': 'category', 'target': 'olap_value_02'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
