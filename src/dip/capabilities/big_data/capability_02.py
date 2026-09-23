"""Big Data Control 02: Distributed processing plans, partitioning and workload controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="big_data.02",
    family="big_data",
    title='Big Data Control 02',
    description='Distributed processing plans, partitioning and workload controls',
    operation="filter_not_null",
    configuration={'field': 'region', 'target': 'big_data_value_02'},
    tags=("big_data", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
