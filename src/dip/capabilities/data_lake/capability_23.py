"""Data Lake Control 23: Raw zone ingestion, partitioning and object lifecycle operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_lake.23",
    family="data_lake",
    title='Data Lake Control 23',
    description='Raw zone ingestion, partitioning and object lifecycle operations',
    operation="project",
    configuration={'field': 'source', 'target': 'data_lake_value_23', 'fields': ['id', 'source', 'value']},
    tags=("data_lake", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
