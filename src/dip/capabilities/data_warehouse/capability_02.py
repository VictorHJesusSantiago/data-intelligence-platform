"""Data Warehouse Control 02: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.02",
    family="data_warehouse",
    title='Data Warehouse Control 02',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="filter_not_null",
    configuration={'field': 'status', 'target': 'data_warehouse_value_02'},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
