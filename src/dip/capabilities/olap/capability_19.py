"""Olap Control 19: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.19",
    family="olap",
    title='Olap Control 19',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="classify",
    configuration={'field': 'region', 'target': 'olap_value_19'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
