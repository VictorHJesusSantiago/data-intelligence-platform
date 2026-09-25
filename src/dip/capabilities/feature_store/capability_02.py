"""Feature Store Control 02: Reusable analytical features and point-in-time consistency rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="feature_store.02",
    family="feature_store",
    title='Feature Store Control 02',
    description='Reusable analytical features and point-in-time consistency rules',
    operation="filter_not_null",
    configuration={'field': 'region', 'target': 'feature_store_value_02'},
    tags=("feature_store", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
