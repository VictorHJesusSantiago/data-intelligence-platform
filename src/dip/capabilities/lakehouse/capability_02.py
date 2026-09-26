"""Lakehouse Control 02: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.02",
    family="lakehouse",
    title='Lakehouse Control 02',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="filter_not_null",
    configuration={'field': 'source', 'target': 'lakehouse_value_02'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
