"""Lakehouse Control 01: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.01",
    family="lakehouse",
    title='Lakehouse Control 01',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="profile",
    configuration={'field': 'amount', 'target': 'lakehouse_value_01'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
