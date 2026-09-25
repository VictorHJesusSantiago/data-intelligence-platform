"""Data Warehouse Control 20: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.20",
    family="data_warehouse",
    title='Data Warehouse Control 20',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="timestamp",
    configuration={'field': 'category', 'target': 'data_warehouse_value_20'},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
