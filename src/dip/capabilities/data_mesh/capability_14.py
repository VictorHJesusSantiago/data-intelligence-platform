"""Data Mesh Control 14: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.14",
    family="data_mesh",
    title='Data Mesh Control 14',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="derive",
    configuration={'field': 'email', 'target': 'data_mesh_value_14', 'factor': 1.14},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
