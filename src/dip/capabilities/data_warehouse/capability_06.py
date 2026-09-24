"""Data Warehouse Control 06: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.06",
    family="data_warehouse",
    title='Data Warehouse Control 06',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_warehouse_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
