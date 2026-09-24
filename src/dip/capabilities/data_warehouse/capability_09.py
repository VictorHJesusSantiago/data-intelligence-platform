"""Data Warehouse Control 09: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.09",
    family="data_warehouse",
    title='Data Warehouse Control 09',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="classify",
    configuration={'field': 'event_time', 'target': 'data_warehouse_value_09'},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
