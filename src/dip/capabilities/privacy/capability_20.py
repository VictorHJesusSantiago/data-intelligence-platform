"""Privacy Control 20: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.20",
    family="privacy",
    title='Privacy Control 20',
    description='Masking, classification, minimization and access transformations',
    operation="timestamp",
    configuration={'field': 'amount', 'target': 'privacy_value_20'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
