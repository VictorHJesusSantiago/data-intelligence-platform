"""Data Lake Control 24: Raw zone ingestion, partitioning and object lifecycle operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_lake.24",
    family="data_lake",
    title='Data Lake Control 24',
    description='Raw zone ingestion, partitioning and object lifecycle operations',
    operation="derive",
    configuration={'field': 'id', 'target': 'data_lake_value_24', 'factor': 1.24},
    tags=("data_lake", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
