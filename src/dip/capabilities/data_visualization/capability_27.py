"""Data Visualization Control 27: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.27",
    family="data_visualization",
    title='Data Visualization Control 27',
    description='Visual encodings, chart preparation and presentation rules',
    operation="dedupe",
    configuration={'field': 'id', 'target': 'data_visualization_value_27'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
