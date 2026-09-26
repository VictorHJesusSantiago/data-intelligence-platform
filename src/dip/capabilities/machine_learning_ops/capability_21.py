"""Machine Learning Ops Control 21: Dataset checks, drift signals and model input preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="machine_learning_ops.21",
    family="machine_learning_ops",
    title='Machine Learning Ops Control 21',
    description='Dataset checks, drift signals and model input preparation',
    operation="profile",
    configuration={'field': 'email', 'target': 'machine_learning_ops_value_21'},
    tags=("machine_learning_ops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
