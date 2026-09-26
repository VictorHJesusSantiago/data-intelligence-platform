"""Privacy Control 27: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.27",
    family="privacy",
    title='Privacy Control 27',
    description='Masking, classification, minimization and access transformations',
    operation="dedupe",
    configuration={'field': 'category', 'target': 'privacy_value_27'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
