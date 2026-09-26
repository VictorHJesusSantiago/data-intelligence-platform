"""Machine Learning Ops Control 17: Dataset checks, drift signals and model input preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="machine_learning_ops.17",
    family="machine_learning_ops",
    title='Machine Learning Ops Control 17',
    description='Dataset checks, drift signals and model input preparation',
    operation="dedupe",
    configuration={'field': 'source', 'target': 'machine_learning_ops_value_17'},
    tags=("machine_learning_ops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
