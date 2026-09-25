"""Data Warehouse Control 14: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.14",
    family="data_warehouse",
    title='Data Warehouse Control 14',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="derive",
    configuration={'field': 'source', 'target': 'data_warehouse_value_14', 'factor': 1.14},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
