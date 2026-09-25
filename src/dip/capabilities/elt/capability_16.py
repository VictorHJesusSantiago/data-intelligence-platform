"""Elt Control 16: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.16",
    family="elt",
    title='Elt Control 16',
    description='Extract, load and in-platform transformation steps',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'elt_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
