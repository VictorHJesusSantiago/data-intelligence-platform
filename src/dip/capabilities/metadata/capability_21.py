"""Metadata Control 21: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.21",
    family="metadata",
    title='Metadata Control 21',
    description='Technical, operational and business metadata processors',
    operation="profile",
    configuration={'field': 'id', 'target': 'metadata_value_21'},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
