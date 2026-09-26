"""Metadata Control 03: Technical, operational and business metadata processors."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="metadata.03",
    family="metadata",
    title='Metadata Control 03',
    description='Technical, operational and business metadata processors',
    operation="project",
    configuration={'field': 'region', 'target': 'metadata_value_03', 'fields': ['id', 'region', 'value']},
    tags=("metadata", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
