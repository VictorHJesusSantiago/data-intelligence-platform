"""Lakehouse Control 08: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.08",
    family="lakehouse",
    title='Lakehouse Control 08',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="mask",
    configuration={'field': 'category', 'target': 'lakehouse_value_08'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
