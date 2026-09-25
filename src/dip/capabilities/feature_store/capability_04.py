"""Feature Store Control 04: Reusable analytical features and point-in-time consistency rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="feature_store.04",
    family="feature_store",
    title='Feature Store Control 04',
    description='Reusable analytical features and point-in-time consistency rules',
    operation="derive",
    configuration={'field': 'event_time', 'target': 'feature_store_value_04', 'factor': 1.04},
    tags=("feature_store", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
