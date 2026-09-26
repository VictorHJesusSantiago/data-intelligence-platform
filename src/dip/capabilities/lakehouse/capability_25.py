"""Lakehouse Control 25: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.25",
    family="lakehouse",
    title='Lakehouse Control 25',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="aggregate",
    configuration={'field': 'region', 'target': 'lakehouse_value_25'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
