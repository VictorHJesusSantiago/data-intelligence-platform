"""Data Fabric Control 01: Federated access, metadata activation and intelligent routing."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_fabric.01",
    family="data_fabric",
    title='Data Fabric Control 01',
    description='Federated access, metadata activation and intelligent routing',
    operation="profile",
    configuration={'field': 'source', 'target': 'data_fabric_value_01'},
    tags=("data_fabric", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
