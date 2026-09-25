"""Feature Store Control 17: Reusable analytical features and point-in-time consistency rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="feature_store.17",
    family="feature_store",
    title='Feature Store Control 17',
    description='Reusable analytical features and point-in-time consistency rules',
    operation="dedupe",
    configuration={'field': 'status', 'target': 'feature_store_value_17'},
    tags=("feature_store", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
