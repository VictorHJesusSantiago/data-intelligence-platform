"""Data Integration Control 20: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.20",
    family="data_integration",
    title='Data Integration Control 20',
    description='Source mapping, normalization and cross-system data exchange',
    operation="timestamp",
    configuration={'field': 'source', 'target': 'data_integration_value_20'},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
