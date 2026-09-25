"""Elt Control 02: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.02",
    family="elt",
    title='Elt Control 02',
    description='Extract, load and in-platform transformation steps',
    operation="filter_not_null",
    configuration={'field': 'email', 'target': 'elt_value_02'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
