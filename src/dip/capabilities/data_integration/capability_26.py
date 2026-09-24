"""Data Integration Control 26: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.26",
    family="data_integration",
    title='Data Integration Control 26',
    description='Source mapping, normalization and cross-system data exchange',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_integration_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
