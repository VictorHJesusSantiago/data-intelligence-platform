"""Data Integration Control 12: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.12",
    family="data_integration",
    title='Data Integration Control 12',
    description='Source mapping, normalization and cross-system data exchange',
    operation="filter_not_null",
    configuration={'field': 'value', 'target': 'data_integration_value_12'},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
