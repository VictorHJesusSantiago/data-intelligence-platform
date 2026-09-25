"""Decision Support Control 14: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.14",
    family="decision_support",
    title='Decision Support Control 14',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="derive",
    configuration={'field': 'amount', 'target': 'decision_support_value_14', 'factor': 1.14},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
