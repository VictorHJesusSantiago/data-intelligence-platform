"""Elt Control 21: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.21",
    family="elt",
    title='Elt Control 21',
    description='Extract, load and in-platform transformation steps',
    operation="profile",
    configuration={'field': 'region', 'target': 'elt_value_21'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
