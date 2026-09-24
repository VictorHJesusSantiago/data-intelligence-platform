"""Data Integration Control 02: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.02",
    family="data_integration",
    title='Data Integration Control 02',
    description='Source mapping, normalization and cross-system data exchange',
    operation="filter_not_null",
    configuration={'field': 'value', 'target': 'data_integration_value_02'},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
