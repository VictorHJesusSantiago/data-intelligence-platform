"""Metadata Control 20: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.20",
    family="metadata",
    title='Metadata Control 20',
    description='Technical, operational and business metadata processors',
    operation="timestamp",
    configuration={'field': 'source', 'target': 'metadata_value_20'},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
