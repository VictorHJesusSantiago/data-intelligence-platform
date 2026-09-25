"""Elt Control 24: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.24",
    family="elt",
    title='Elt Control 24',
    description='Extract, load and in-platform transformation steps',
    operation="derive",
    configuration={'field': 'category', 'target': 'elt_value_24', 'factor': 1.24},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
