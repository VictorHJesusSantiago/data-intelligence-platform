"""Data Mesh Control 01: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.01",
    family="data_mesh",
    title='Data Mesh Control 01',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="profile",
    configuration={'field': 'id', 'target': 'data_mesh_value_01'},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
