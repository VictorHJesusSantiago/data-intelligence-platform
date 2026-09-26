"""Privacy Control 13: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.13",
    family="privacy",
    title='Privacy Control 13',
    description='Masking, classification, minimization and access transformations',
    operation="project",
    configuration={'field': 'value', 'target': 'privacy_value_13', 'fields': ['id', 'value', 'value']},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
