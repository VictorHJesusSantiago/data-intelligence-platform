"""Olap Control 30: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.30",
    family="olap",
    title='Olap Control 30',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="timestamp",
    configuration={'field': 'email', 'target': 'olap_value_30'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
