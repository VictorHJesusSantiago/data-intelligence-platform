"""Data Lake Control 07: Raw zone ingestion, partitioning and object lifecycle operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_lake.07",
    family="data_lake",
    title='Data Lake Control 07',
    description='Raw zone ingestion, partitioning and object lifecycle operations',
    operation="dedupe",
    configuration={'field': 'email', 'target': 'data_lake_value_07'},
    tags=("data_lake", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
