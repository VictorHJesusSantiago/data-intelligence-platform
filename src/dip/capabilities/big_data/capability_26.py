"""Big Data Control 26: Distributed processing plans, partitioning and workload controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="big_data.26",
    family="big_data",
    title='Big Data Control 26',
    description='Distributed processing plans, partitioning and workload controls',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'big_data_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("big_data", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
