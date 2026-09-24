"""Data Integration Control 01: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.01",
    family="data_integration",
    title='Data Integration Control 01',
    description='Source mapping, normalization and cross-system data exchange',
    operation="profile",
    configuration={'field': 'id', 'target': 'data_integration_value_01'},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
