"""Lakehouse Control 11: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.11",
    family="lakehouse",
    title='Lakehouse Control 11',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="profile",
    configuration={'field': 'amount', 'target': 'lakehouse_value_11'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
