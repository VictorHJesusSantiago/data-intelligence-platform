"""Olap Control 11: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.11",
    family="olap",
    title='Olap Control 11',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="profile",
    configuration={'field': 'event_time', 'target': 'olap_value_11'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
