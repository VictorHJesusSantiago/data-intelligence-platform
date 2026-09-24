"""Data Mesh Control 29: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.29",
    family="data_mesh",
    title='Data Mesh Control 29',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="classify",
    configuration={'field': 'amount', 'target': 'data_mesh_value_29'},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
