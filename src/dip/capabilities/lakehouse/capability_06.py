"""Lakehouse Control 06: Transactional lake tables, medallion layers and table optimization."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="lakehouse.06",
    family="lakehouse",
    title='Lakehouse Control 06',
    description='Transactional lake tables, medallion layers and table optimization',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'lakehouse_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("lakehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
