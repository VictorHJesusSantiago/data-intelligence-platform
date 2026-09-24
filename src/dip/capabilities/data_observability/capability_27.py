"""Data Observability Control 27: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.27",
    family="data_observability",
    title='Data Observability Control 27',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="dedupe",
    configuration={'field': 'event_time', 'target': 'data_observability_value_27'},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
