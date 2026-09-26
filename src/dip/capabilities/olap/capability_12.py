"""Olap Control 12: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.12",
    family="olap",
    title='Olap Control 12',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="filter_not_null",
    configuration={'field': 'category', 'target': 'olap_value_12'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
