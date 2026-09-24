"""Data Visualization Control 25: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.25",
    family="data_visualization",
    title='Data Visualization Control 25',
    description='Visual encodings, chart preparation and presentation rules',
    operation="aggregate",
    configuration={'field': 'amount', 'target': 'data_visualization_value_25'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
