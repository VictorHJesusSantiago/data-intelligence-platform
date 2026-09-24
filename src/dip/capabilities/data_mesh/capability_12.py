"""Data Mesh Control 12: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.12",
    family="data_mesh",
    title='Data Mesh Control 12',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="filter_not_null",
    configuration={'field': 'value', 'target': 'data_mesh_value_12'},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
