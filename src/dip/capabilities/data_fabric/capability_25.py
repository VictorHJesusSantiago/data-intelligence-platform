"""Data Fabric Control 25: Federated access, metadata activation and intelligent routing."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_fabric.25",
    family="data_fabric",
    title='Data Fabric Control 25',
    description='Federated access, metadata activation and intelligent routing',
    operation="aggregate",
    configuration={'field': 'email', 'target': 'data_fabric_value_25'},
    tags=("data_fabric", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
