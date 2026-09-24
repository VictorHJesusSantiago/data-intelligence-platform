"""Data Visualization Control 21: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.21",
    family="data_visualization",
    title='Data Visualization Control 21',
    description='Visual encodings, chart preparation and presentation rules',
    operation="profile",
    configuration={'field': 'event_time', 'target': 'data_visualization_value_21'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
