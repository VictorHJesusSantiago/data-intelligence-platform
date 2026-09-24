"""Data Visualization Control 22: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.22",
    family="data_visualization",
    title='Data Visualization Control 22',
    description='Visual encodings, chart preparation and presentation rules',
    operation="filter_not_null",
    configuration={'field': 'category', 'target': 'data_visualization_value_22'},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
