"""Elt Control 29: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.29",
    family="elt",
    title='Elt Control 29',
    description='Extract, load and in-platform transformation steps',
    operation="classify",
    configuration={'field': 'id', 'target': 'elt_value_29'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
