"""Data Fabric Control 03: Federated access, metadata activation and intelligent routing."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_fabric.03",
    family="data_fabric",
    title='Data Fabric Control 03',
    description='Federated access, metadata activation and intelligent routing',
    operation="project",
    configuration={'field': 'value', 'target': 'data_fabric_value_03', 'fields': ['id', 'value', 'value']},
    tags=("data_fabric", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
