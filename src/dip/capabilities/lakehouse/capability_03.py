"""Lakehouse Control 03: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.03",
    family="lakehouse",
    title='Lakehouse Control 03',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="project",
    configuration={'field': 'id', 'target': 'lakehouse_value_03', 'fields': ['id', 'id', 'value']},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
