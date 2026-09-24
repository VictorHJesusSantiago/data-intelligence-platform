"""Data Observability Control 19: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.19",
    family="data_observability",
    title='Data Observability Control 19',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="classify",
    configuration={'field': 'owner', 'target': 'data_observability_value_19'},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
