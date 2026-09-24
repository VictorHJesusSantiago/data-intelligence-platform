"""Data Visualization Control 04: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.04",
    family="data_visualization",
    title='Data Visualization Control 04',
    description='Visual encodings, chart preparation and presentation rules',
    operation="derive",
    configuration={'field': 'status', 'target': 'data_visualization_value_04', 'factor': 1.04},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
