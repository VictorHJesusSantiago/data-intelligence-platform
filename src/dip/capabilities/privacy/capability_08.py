"""Privacy Control 08: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.08",
    family="privacy",
    title='Privacy Control 08',
    description='Masking, classification, minimization and access transformations',
    operation="mask",
    configuration={'field': 'owner', 'target': 'privacy_value_08'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
