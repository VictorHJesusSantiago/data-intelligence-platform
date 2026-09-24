"""Data Mesh Control 25: Domain products, contracts, discoverability and self-service controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_mesh.25",
    family="data_mesh",
    title='Data Mesh Control 25',
    description='Domain products, contracts, discoverability and self-service controls',
    operation="aggregate",
    configuration={'field': 'event_time', 'target': 'data_mesh_value_25'},
    tags=("data_mesh", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
