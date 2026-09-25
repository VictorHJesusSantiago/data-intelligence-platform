"""Data Warehouse Control 23: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.23",
    family="data_warehouse",
    title='Data Warehouse Control 23',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="project",
    configuration={'field': 'amount', 'target': 'data_warehouse_value_23', 'fields': ['id', 'amount', 'value']},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
