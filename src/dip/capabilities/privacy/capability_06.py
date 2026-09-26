"""Privacy Control 06: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.06",
    family="privacy",
    title='Privacy Control 06',
    description='Masking, classification, minimization and access transformations',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'privacy_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
