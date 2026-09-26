"""Lakehouse Control 30: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.30",
    family="lakehouse",
    title='Lakehouse Control 30',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="timestamp",
    configuration={'field': 'status', 'target': 'lakehouse_value_30'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
