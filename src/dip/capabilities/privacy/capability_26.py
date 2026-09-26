"""Privacy Control 26: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.26",
    family="privacy",
    title='Privacy Control 26',
    description='Masking, classification, minimization and access transformations',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'privacy_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
