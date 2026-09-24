"""Data Observability Control 15: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.15",
    family="data_observability",
    title='Data Observability Control 15',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="aggregate",
    configuration={'field': 'region', 'target': 'data_observability_value_15'},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
