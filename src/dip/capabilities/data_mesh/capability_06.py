"""Data Mesh Control 06: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.06",
    family="data_mesh",
    title='Data Mesh Control 06',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_mesh_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
