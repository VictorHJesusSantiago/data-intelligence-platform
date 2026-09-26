"""Lakehouse Control 24: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.24",
    family="lakehouse",
    title='Lakehouse Control 24',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="derive",
    configuration={'field': 'value', 'target': 'lakehouse_value_24', 'factor': 1.24},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
