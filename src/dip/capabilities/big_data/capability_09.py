"""Big Data Control 09: Distributed processing plans, partitioning and workload controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="big_data.09",
    family="big_data",
    title='Big Data Control 09',
    description='Distributed processing plans, partitioning and workload controls',
    operation="classify",
    configuration={'field': 'source', 'target': 'big_data_value_09'},
    tags=("big_data", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
