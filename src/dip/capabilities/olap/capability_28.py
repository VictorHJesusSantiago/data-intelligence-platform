"""Olap Control 28: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.28",
    family="olap",
    title='Olap Control 28',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="mask",
    configuration={'field': 'value', 'target': 'olap_value_28'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
