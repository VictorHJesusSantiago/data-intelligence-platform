"""Data Visualization Control 03: Visual encodings, chart preparation and presentation rules."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_visualization.03",
    family="data_visualization",
    title='Data Visualization Control 03',
    description='Visual encodings, chart preparation and presentation rules',
    operation="project",
    configuration={'field': 'owner', 'target': 'data_visualization_value_03', 'fields': ['id', 'owner', 'value']},
    tags=("data_visualization", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
