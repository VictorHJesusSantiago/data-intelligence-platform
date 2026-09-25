"""Data Warehouse Control 22: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.22",
    family="data_warehouse",
    title='Data Warehouse Control 22',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="filter_not_null",
    configuration={'field': 'status', 'target': 'data_warehouse_value_22'},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
