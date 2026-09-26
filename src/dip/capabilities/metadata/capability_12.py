"""Metadata Control 12: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.12",
    family="metadata",
    title='Metadata Control 12',
    description='Technical, operational and business metadata processors',
    operation="filter_not_null",
    configuration={'field': 'value', 'target': 'metadata_value_12'},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
