"""Complex Event Processing Control 05: Patterns, temporal correlations and event-driven alerts."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="complex_event_processing.05",
    family="complex_event_processing",
    title='Complex Event Processing Control 05',
    description='Patterns, temporal correlations and event-driven alerts',
    operation="aggregate",
    configuration={'field': 'status', 'target': 'complex_event_processing_value_05'},
    tags=("complex_event_processing", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
