"""Data Mesh Control 26: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.26",
    family="data_mesh",
    title='Data Mesh Control 26',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_mesh_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
