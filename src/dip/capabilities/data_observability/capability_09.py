"""Data Observability Control 09: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.09",
    family="data_observability",
    title='Data Observability Control 09',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="classify",
    configuration={'field': 'owner', 'target': 'data_observability_value_09'},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
