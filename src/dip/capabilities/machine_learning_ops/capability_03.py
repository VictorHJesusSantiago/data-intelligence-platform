"""Machine Learning Ops Control 03: Dataset checks, drift signals and model input preparation."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="machine_learning_ops.03",
    family="machine_learning_ops",
    title='Machine Learning Ops Control 03',
    description='Dataset checks, drift signals and model input preparation',
    operation="project",
    configuration={'field': 'category', 'target': 'machine_learning_ops_value_03', 'fields': ['id', 'category', 'value']},
    tags=("machine_learning_ops", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
