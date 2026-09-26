"""Privacy Control 09: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.09",
    family="privacy",
    title='Privacy Control 09',
    description='Masking, classification, minimization and access transformations',
    operation="classify",
    configuration={'field': 'status', 'target': 'privacy_value_09'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
