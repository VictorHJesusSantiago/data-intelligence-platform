"""Metadata Control 29: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.29",
    family="metadata",
    title='Metadata Control 29',
    description='Technical, operational and business metadata processors',
    operation="classify",
    configuration={'field': 'amount', 'target': 'metadata_value_29'},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
