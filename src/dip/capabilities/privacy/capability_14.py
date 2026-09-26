"""Privacy Control 14: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.14",
    family="privacy",
    title='Privacy Control 14',
    description='Masking, classification, minimization and access transformations',
    operation="derive",
    configuration={'field': 'region', 'target': 'privacy_value_14', 'factor': 1.14},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
