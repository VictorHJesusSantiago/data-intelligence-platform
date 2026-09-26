"""Privacy Control 07: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.07",
    family="privacy",
    title='Privacy Control 07',
    description='Masking, classification, minimization and access transformations',
    operation="dedupe",
    configuration={'field': 'category', 'target': 'privacy_value_07'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
