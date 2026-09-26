"""Privacy Control 10: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.10",
    family="privacy",
    title='Privacy Control 10',
    description='Masking, classification, minimization and access transformations',
    operation="timestamp",
    configuration={'field': 'amount', 'target': 'privacy_value_10'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
