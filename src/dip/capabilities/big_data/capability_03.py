"""Big Data Control 03: Distributed processing plans, partitioning and workload controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="big_data.03",
    family="big_data",
    title='Big Data Control 03',
    description='Distributed processing plans, partitioning and workload controls',
    operation="project",
    configuration={'field': 'email', 'target': 'big_data_value_03', 'fields': ['id', 'email', 'value']},
    tags=("big_data", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
