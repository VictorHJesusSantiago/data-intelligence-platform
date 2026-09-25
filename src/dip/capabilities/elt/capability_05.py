"""Elt Control 05: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.05",
    family="elt",
    title='Elt Control 05',
    description='Extract, load and in-platform transformation steps',
    operation="aggregate",
    configuration={'field': 'owner', 'target': 'elt_value_05'},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
