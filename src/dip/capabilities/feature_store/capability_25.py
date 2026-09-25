"""Feature Store Control 25: Reusable analytical features and point-in-time consistency rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="feature_store.25",
    family="feature_store",
    title='Feature Store Control 25',
    description='Reusable analytical features and point-in-time consistency rules',
    operation="aggregate",
    configuration={'field': 'category', 'target': 'feature_store_value_25'},
    tags=("feature_store", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
