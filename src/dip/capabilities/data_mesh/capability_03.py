"""Data Mesh Control 03: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.03",
    family="data_mesh",
    title='Data Mesh Control 03',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="project",
    configuration={'field': 'region', 'target': 'data_mesh_value_03', 'fields': ['id', 'region', 'value']},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
