"""Metadata Control 26: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.26",
    family="metadata",
    title='Metadata Control 26',
    description='Technical, operational and business metadata processors',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'metadata_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
