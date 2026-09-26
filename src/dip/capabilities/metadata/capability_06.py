"""Metadata Control 06: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.06",
    family="metadata",
    title='Metadata Control 06',
    description='Technical, operational and business metadata processors',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'metadata_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
