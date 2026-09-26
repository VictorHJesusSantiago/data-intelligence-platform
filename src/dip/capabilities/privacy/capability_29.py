"""Privacy Control 29: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.29",
    family="privacy",
    title='Privacy Control 29',
    description='Masking, classification, minimization and access transformations',
    operation="classify",
    configuration={'field': 'status', 'target': 'privacy_value_29'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
