"""Big Data Control 24: Distributed processing plans, partitioning and workload controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="big_data.24",
    family="big_data",
    title='Big Data Control 24',
    description='Distributed processing plans, partitioning and workload controls',
    operation="derive",
    configuration={'field': 'event_time', 'target': 'big_data_value_24', 'factor': 1.24},
    tags=("big_data", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
