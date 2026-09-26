"""Olap Control 16: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.16",
    family="olap",
    title='Olap Control 16',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'olap_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
