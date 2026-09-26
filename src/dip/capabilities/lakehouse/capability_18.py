"""Lakehouse Control 18: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.18",
    family="lakehouse",
    title='Lakehouse Control 18',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="mask",
    configuration={'field': 'category', 'target': 'lakehouse_value_18'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
