"""Data Mesh Control 30: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.30",
    family="data_mesh",
    title='Data Mesh Control 30',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="timestamp",
    configuration={'field': 'source', 'target': 'data_mesh_value_30'},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
