"""Metadata Control 15: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.15",
    family="metadata",
    title='Metadata Control 15',
    description='Technical, operational and business metadata processors',
    operation="aggregate",
    configuration={'field': 'event_time', 'target': 'metadata_value_15'},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
