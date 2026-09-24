"""Data Visualization Control 14: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.14",
    family="data_visualization",
    title='Data Visualization Control 14',
    description='Visual encodings, chart preparation and presentation rules',
    operation="derive",
    configuration={'field': 'status', 'target': 'data_visualization_value_14', 'factor': 1.14},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
