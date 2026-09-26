"""Privacy Control 04: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.04",
    family="privacy",
    title='Privacy Control 04',
    description='Masking, classification, minimization and access transformations',
    operation="derive",
    configuration={'field': 'region', 'target': 'privacy_value_04', 'factor': 1.04},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
