"""Metadata Control 08: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.08",
    family="metadata",
    title='Metadata Control 08',
    description='Technical, operational and business metadata processors',
    operation="mask",
    configuration={'field': 'status', 'target': 'metadata_value_08'},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
