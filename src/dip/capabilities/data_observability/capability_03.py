"""Data Observability Control 03: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.03",
    family="data_observability",
    title='Data Observability Control 03',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="project",
    configuration={'field': 'id', 'target': 'data_observability_value_03', 'fields': ['id', 'id', 'value']},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
