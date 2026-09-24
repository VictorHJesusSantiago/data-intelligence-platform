"""Data Lake Control 17: Raw zone ingestion, partitioning and object lifecycle operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_lake.17",
    family="data_lake",
    title='Data Lake Control 17',
    description='Raw zone ingestion, partitioning and object lifecycle operations',
    operation="dedupe",
    configuration={'field': 'email', 'target': 'data_lake_value_17'},
    tags=("data_lake", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
