"""Machine Learning Ops Control 26: Dataset checks, drift signals and model input preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="machine_learning_ops.26",
    family="machine_learning_ops",
    title='Machine Learning Ops Control 26',
    description='Dataset checks, drift signals and model input preparation',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'machine_learning_ops_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("machine_learning_ops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
