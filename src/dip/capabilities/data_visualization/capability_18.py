"""Data Visualization Control 18: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.18",
    family="data_visualization",
    title='Data Visualization Control 18',
    description='Visual encodings, chart preparation and presentation rules',
    operation="mask",
    configuration={'field': 'value', 'target': 'data_visualization_value_18'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
