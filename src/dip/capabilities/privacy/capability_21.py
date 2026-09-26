"""Privacy Control 21: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.21",
    family="privacy",
    title='Privacy Control 21',
    description='Masking, classification, minimization and access transformations',
    operation="profile",
    configuration={'field': 'source', 'target': 'privacy_value_21'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
