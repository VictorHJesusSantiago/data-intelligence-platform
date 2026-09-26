"""Privacy Control 23: Masking, classification, minimization and access transformations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="privacy.23",
    family="privacy",
    title='Privacy Control 23',
    description='Masking, classification, minimization and access transformations',
    operation="project",
    configuration={'field': 'value', 'target': 'privacy_value_23', 'fields': ['id', 'value', 'value']},
    tags=("privacy", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
