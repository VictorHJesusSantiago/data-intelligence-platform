"""Data Visualization Control 12: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.12",
    family="data_visualization",
    title='Data Visualization Control 12',
    description='Visual encodings, chart preparation and presentation rules',
    operation="filter_not_null",
    configuration={'field': 'category', 'target': 'data_visualization_value_12'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
