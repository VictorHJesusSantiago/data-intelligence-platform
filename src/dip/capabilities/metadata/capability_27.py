"""Metadata Control 27: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.27",
    family="metadata",
    title='Metadata Control 27',
    description='Technical, operational and business metadata processors',
    operation="dedupe",
    configuration={'field': 'owner', 'target': 'metadata_value_27'},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
