"""Lakehouse Control 14: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.14",
    family="lakehouse",
    title='Lakehouse Control 14',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="derive",
    configuration={'field': 'value', 'target': 'lakehouse_value_14', 'factor': 1.14},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
