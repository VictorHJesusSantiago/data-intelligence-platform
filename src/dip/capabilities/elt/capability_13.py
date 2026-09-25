"""Elt Control 13: Extract, load and in-platform transformation steps."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="elt.13",
    family="elt",
    title='Elt Control 13',
    description='Extract, load and in-platform transformation steps',
    operation="project",
    configuration={'field': 'event_time', 'target': 'elt_value_13', 'fields': ['id', 'event_time', 'value']},
    tags=("elt", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
