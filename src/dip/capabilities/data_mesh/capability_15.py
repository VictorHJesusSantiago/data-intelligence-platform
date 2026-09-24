"""Data Mesh Control 15: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.15",
    family="data_mesh",
    title='Data Mesh Control 15',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="aggregate",
    configuration={'field': 'event_time', 'target': 'data_mesh_value_15'},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
