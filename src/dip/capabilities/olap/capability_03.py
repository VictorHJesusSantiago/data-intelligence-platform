"""Olap Control 03: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.03",
    family="olap",
    title='Olap Control 03',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="project",
    configuration={'field': 'owner', 'target': 'olap_value_03', 'fields': ['id', 'owner', 'value']},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
