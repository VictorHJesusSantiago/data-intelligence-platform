"""Olap Control 10: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.10",
    family="olap",
    title='Olap Control 10',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="timestamp",
    configuration={'field': 'email', 'target': 'olap_value_10'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
