"""Data Integration Control 18: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.18",
    family="data_integration",
    title='Data Integration Control 18',
    description='Source mapping, normalization and cross-system data exchange',
    operation="mask",
    configuration={'field': 'status', 'target': 'data_integration_value_18'},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
