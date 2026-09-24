"""Data Mesh Control 17: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.17",
    family="data_mesh",
    title='Data Mesh Control 17',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="dedupe",
    configuration={'field': 'owner', 'target': 'data_mesh_value_17'},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
