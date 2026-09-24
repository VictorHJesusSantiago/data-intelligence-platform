"""Data Visualization Control 16: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.16",
    family="data_visualization",
    title='Data Visualization Control 16',
    description='Visual encodings, chart preparation and presentation rules',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_visualization_value_16', 'minimum': 0, 'maximum': 1000016},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
