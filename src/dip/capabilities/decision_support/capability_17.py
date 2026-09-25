"""Decision Support Control 17: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.17",
    family="decision_support",
    title='Decision Support Control 17',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="dedupe",
    configuration={'field': 'value', 'target': 'decision_support_value_17'},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
