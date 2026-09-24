"""Data Visualization Control 19: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.19",
    family="data_visualization",
    title='Data Visualization Control 19',
    description='Visual encodings, chart preparation and presentation rules',
    operation="classify",
    configuration={'field': 'region', 'target': 'data_visualization_value_19'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
