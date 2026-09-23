"""Big Data Control 14: Distributed processing plans, partitioning and workload controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="big_data.14",
    family="big_data",
    title='Big Data Control 14',
    description='Distributed processing plans, partitioning and workload controls',
    operation="derive",
    configuration={'field': 'event_time', 'target': 'big_data_value_14', 'factor': 1.14},
    tags=("big_data", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
