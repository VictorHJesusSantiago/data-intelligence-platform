"""Lakehouse Control 07: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.07",
    family="lakehouse",
    title='Lakehouse Control 07',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="dedupe",
    configuration={'field': 'event_time', 'target': 'lakehouse_value_07'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
