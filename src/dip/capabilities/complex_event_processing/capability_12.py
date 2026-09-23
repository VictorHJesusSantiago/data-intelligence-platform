"""Complex Event Processing Control 12: Patterns, temporal correlations and event-driven alerts."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="complex_event_processing.12",
    family="complex_event_processing",
    title='Complex Event Processing Control 12',
    description='Patterns, temporal correlations and event-driven alerts',
    operation="filter_not_null",
    configuration={'field': 'event_time', 'target': 'complex_event_processing_value_12'},
    tags=("complex_event_processing", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
