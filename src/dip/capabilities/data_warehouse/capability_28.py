"""Data Warehouse Control 28: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.28",
    family="data_warehouse",
    title='Data Warehouse Control 28',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="mask",
    configuration={'field': 'email', 'target': 'data_warehouse_value_28'},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
