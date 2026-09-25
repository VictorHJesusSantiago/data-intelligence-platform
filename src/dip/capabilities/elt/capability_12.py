"""Elt Control 12: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.12",
    family="elt",
    title='Elt Control 12',
    description='Extract, load and in-platform transformation steps',
    operation="filter_not_null",
    configuration={'field': 'email', 'target': 'elt_value_12'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
