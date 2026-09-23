"""Big Data Control 05: Distributed processing plans, partitioning and workload controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="big_data.05",
    family="big_data",
    title='Big Data Control 05',
    description='Distributed processing plans, partitioning and workload controls',
    operation="aggregate",
    configuration={'field': 'category', 'target': 'big_data_value_05'},
    tags=("big_data", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
