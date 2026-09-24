"""Data Visualization Control 29: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.29",
    family="data_visualization",
    title='Data Visualization Control 29',
    description='Visual encodings, chart preparation and presentation rules',
    operation="classify",
    configuration={'field': 'region', 'target': 'data_visualization_value_29'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
