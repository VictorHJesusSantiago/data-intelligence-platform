"""Data Observability Control 30: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.30",
    family="data_observability",
    title='Data Observability Control 30',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="timestamp",
    configuration={'field': 'status', 'target': 'data_observability_value_30'},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
