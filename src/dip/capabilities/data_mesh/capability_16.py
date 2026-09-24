"""Data Mesh Control 16: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.16",
    family="data_mesh",
    title='Data Mesh Control 16',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_mesh_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
