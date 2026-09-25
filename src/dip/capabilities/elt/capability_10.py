"""Elt Control 10: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.10",
    family="elt",
    title='Elt Control 10',
    description='Extract, load and in-platform transformation steps',
    operation="timestamp",
    configuration={'field': 'value', 'target': 'elt_value_10'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
