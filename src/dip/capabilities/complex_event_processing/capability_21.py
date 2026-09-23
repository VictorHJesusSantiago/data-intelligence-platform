"""Complex Event Processing Control 21: Patterns, temporal correlations and event-driven alerts."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="complex_event_processing.21",
    family="complex_event_processing",
    title='Complex Event Processing Control 21',
    description='Patterns, temporal correlations and event-driven alerts',
    operation="profile",
    configuration={'field': 'email', 'target': 'complex_event_processing_value_21'},
    tags=("complex_event_processing", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
