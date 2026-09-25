"""Feature Store Control 13: Reusable analytical features and point-in-time consistency rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="feature_store.13",
    family="feature_store",
    title='Feature Store Control 13',
    description='Reusable analytical features and point-in-time consistency rules',
    operation="project",
    configuration={'field': 'email', 'target': 'feature_store_value_13', 'fields': ['id', 'email', 'value']},
    tags=("feature_store", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
