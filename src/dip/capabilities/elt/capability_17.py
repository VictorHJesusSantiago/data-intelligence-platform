"""Elt Control 17: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.17",
    family="elt",
    title='Elt Control 17',
    description='Extract, load and in-platform transformation steps',
    operation="dedupe",
    configuration={'field': 'amount', 'target': 'elt_value_17'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
