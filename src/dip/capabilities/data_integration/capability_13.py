"""Data Integration Control 13: Source mapping, normalization and cross-system data exchange."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_integration.13",
    family="data_integration",
    title='Data Integration Control 13',
    description='Source mapping, normalization and cross-system data exchange',
    operation="project",
    configuration={'field': 'region', 'target': 'data_integration_value_13', 'fields': ['id', 'region', 'value']},
    tags=("data_integration", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
