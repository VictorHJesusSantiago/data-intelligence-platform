"""Data Integration Control 04: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.04",
    family="data_integration",
    title='Data Integration Control 04',
    description='Source mapping, normalization and cross-system data exchange',
    operation="derive",
    configuration={'field': 'email', 'target': 'data_integration_value_04', 'factor': 1.04},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
