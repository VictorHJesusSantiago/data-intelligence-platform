"""Lakehouse Control 21: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.21",
    family="lakehouse",
    title='Lakehouse Control 21',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="profile",
    configuration={'field': 'amount', 'target': 'lakehouse_value_21'},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
