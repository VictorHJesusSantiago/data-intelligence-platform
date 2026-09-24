"""Data Lake Control 02: Raw zone ingestion, partitioning and object lifecycle operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_lake.02",
    family="data_lake",
    title='Data Lake Control 02',
    description='Raw zone ingestion, partitioning and object lifecycle operations',
    operation="filter_not_null",
    configuration={'field': 'amount', 'target': 'data_lake_value_02'},
    tags=("data_lake", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
