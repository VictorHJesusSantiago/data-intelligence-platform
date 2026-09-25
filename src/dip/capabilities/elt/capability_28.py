"""Elt Control 28: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.28",
    family="elt",
    title='Elt Control 28',
    description='Extract, load and in-platform transformation steps',
    operation="mask",
    configuration={'field': 'source', 'target': 'elt_value_28'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
