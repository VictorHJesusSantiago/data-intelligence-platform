"""Data Observability Control 06: Freshness, volume, schema, lineage and distribution monitoring."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_observability.06",
    family="data_observability",
    title='Data Observability Control 06',
    description='Freshness, volume, schema, lineage and distribution monitoring',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_observability_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("data_observability", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
