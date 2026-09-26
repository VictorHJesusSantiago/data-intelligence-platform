"""Lakehouse Control 09: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.09",
    family="lakehouse",
    title='Lakehouse Control 09',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="classify",
    configuration={'field': 'owner', 'target': 'lakehouse_value_09'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
