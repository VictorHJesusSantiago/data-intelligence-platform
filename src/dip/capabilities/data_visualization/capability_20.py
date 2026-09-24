"""Data Visualization Control 20: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.20",
    family="data_visualization",
    title='Data Visualization Control 20',
    description='Visual encodings, chart preparation and presentation rules',
    operation="timestamp",
    configuration={'field': 'email', 'target': 'data_visualization_value_20'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
