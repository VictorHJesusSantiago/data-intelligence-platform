"""Data Observability Control 02: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.02",
    family="data_observability",
    title='Data Observability Control 02',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="filter_not_null",
    configuration={'field': 'source', 'target': 'data_observability_value_02'},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
