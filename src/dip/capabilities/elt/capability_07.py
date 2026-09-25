"""Elt Control 07: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.07",
    family="elt",
    title='Elt Control 07',
    description='Extract, load and in-platform transformation steps',
    operation="dedupe",
    configuration={'field': 'amount', 'target': 'elt_value_07'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
