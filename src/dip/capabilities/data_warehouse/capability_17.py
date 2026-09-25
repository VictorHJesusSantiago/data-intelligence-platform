"""Data Warehouse Control 17: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.17",
    family="data_warehouse",
    title='Data Warehouse Control 17',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="dedupe",
    configuration={'field': 'region', 'target': 'data_warehouse_value_17'},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
