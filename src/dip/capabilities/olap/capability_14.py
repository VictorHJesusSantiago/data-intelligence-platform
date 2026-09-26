"""Olap Control 14: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.14",
    family="olap",
    title='Olap Control 14',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="derive",
    configuration={'field': 'status', 'target': 'olap_value_14', 'factor': 1.14},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
