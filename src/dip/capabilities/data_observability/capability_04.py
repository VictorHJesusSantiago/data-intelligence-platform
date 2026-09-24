"""Data Observability Control 04: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.04",
    family="data_observability",
    title='Data Observability Control 04',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="derive",
    configuration={'field': 'value', 'target': 'data_observability_value_04', 'factor': 1.04},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
