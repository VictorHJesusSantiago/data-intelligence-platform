"""Privacy Control 12: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.12",
    family="privacy",
    title='Privacy Control 12',
    description='Masking, classification, minimization and access transformations',
    operation="filter_not_null",
    configuration={'field': 'id', 'target': 'privacy_value_12'},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
