"""Data Warehouse Control 13: Dimensional models, facts, dimensions and warehouse loading."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_warehouse.13",
    family="data_warehouse",
    title='Data Warehouse Control 13',
    description='Dimensional models, facts, dimensions and warehouse loading',
    operation="project",
    configuration={'field': 'amount', 'target': 'data_warehouse_value_13', 'fields': ['id', 'amount', 'value']},
    tags=("data_warehouse", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
