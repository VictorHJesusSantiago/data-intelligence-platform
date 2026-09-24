"""Data Lake Control 06: Raw zone ingestion, partitioning and object lifecycle operations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_lake.06",
    family="data_lake",
    title='Data Lake Control 06',
    description='Raw zone ingestion, partitioning and object lifecycle operations',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'data_lake_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("data_lake", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
