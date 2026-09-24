"""Data Visualization Control 17: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.17",
    family="data_visualization",
    title='Data Visualization Control 17',
    description='Visual encodings, chart preparation and presentation rules',
    operation="dedupe",
    configuration={'field': 'id', 'target': 'data_visualization_value_17'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
