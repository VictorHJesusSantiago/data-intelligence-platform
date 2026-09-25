"""Feature Store Control 26: Reusable analytical features and point-in-time consistency rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="feature_store.26",
    family="feature_store",
    title='Feature Store Control 26',
    description='Reusable analytical features and point-in-time consistency rules',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'feature_store_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("feature_store", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
