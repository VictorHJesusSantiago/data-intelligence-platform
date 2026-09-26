"""Machine Learning Ops Control 24: Dataset checks, drift signals and model input preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="machine_learning_ops.24",
    family="machine_learning_ops",
    title='Machine Learning Ops Control 24',
    description='Dataset checks, drift signals and model input preparation',
    operation="derive",
    configuration={'field': 'owner', 'target': 'machine_learning_ops_value_24', 'factor': 1.24},
    tags=("machine_learning_ops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
