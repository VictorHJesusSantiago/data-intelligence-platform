"""Olap Control 22: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.22",
    family="olap",
    title='Olap Control 22',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="filter_not_null",
    configuration={'field': 'category', 'target': 'olap_value_22'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
