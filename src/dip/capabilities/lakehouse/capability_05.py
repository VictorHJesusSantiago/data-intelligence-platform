"""Lakehouse Control 05: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.05",
    family="lakehouse",
    title='Lakehouse Control 05',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="aggregate",
    configuration={'field': 'region', 'target': 'lakehouse_value_05'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
