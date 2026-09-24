"""Data Lake Control 15: Raw zone ingestion, partitioning and object lifecycle operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_lake.15",
    family="data_lake",
    title='Data Lake Control 15',
    description='Raw zone ingestion, partitioning and object lifecycle operations',
    operation="aggregate",
    configuration={'field': 'value', 'target': 'data_lake_value_15'},
    tags=("data_lake", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
