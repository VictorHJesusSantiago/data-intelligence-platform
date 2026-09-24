"""Data Integration Control 28: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.28",
    family="data_integration",
    title='Data Integration Control 28',
    description='Source mapping, normalization and cross-system data exchange',
    operation="mask",
    configuration={'field': 'status', 'target': 'data_integration_value_28'},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
