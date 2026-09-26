"""Privacy Control 15: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.15",
    family="privacy",
    title='Privacy Control 15',
    description='Masking, classification, minimization and access transformations',
    operation="aggregate",
    configuration={'field': 'email', 'target': 'privacy_value_15'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
