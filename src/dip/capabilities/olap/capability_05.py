"""Olap Control 05: Cubes, dimensions, hierarchies, measures and analytical slices."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="olap.05",
    family="olap",
    title='Olap Control 05',
    description='Cubes, dimensions, hierarchies, measures and analytical slices',
    operation="aggregate",
    configuration={'field': 'amount', 'target': 'olap_value_05'},
    tags=("olap", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
