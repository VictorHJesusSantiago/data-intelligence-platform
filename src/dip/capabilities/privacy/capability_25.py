"""Privacy Control 25: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.25",
    family="privacy",
    title='Privacy Control 25',
    description='Masking, classification, minimization and access transformations',
    operation="aggregate",
    configuration={'field': 'email', 'target': 'privacy_value_25'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
