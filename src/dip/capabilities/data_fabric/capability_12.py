"""Data Fabric Control 12: Federated access, metadata activation and intelligent routing."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_fabric.12",
    family="data_fabric",
    title='Data Fabric Control 12',
    description='Federated access, metadata activation and intelligent routing',
    operation="filter_not_null",
    configuration={'field': 'id', 'target': 'data_fabric_value_12'},
    tags=("data_fabric", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
