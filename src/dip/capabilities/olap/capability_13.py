"""Olap Control 13: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.13",
    family="olap",
    title='Olap Control 13',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="project",
    configuration={'field': 'owner', 'target': 'olap_value_13', 'fields': ['id', 'owner', 'value']},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
