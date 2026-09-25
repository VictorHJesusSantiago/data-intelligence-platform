"""Decision Support Control 11: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.11",
    family="decision_support",
    title='Decision Support Control 11',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="profile",
    configuration={'field': 'category', 'target': 'decision_support_value_11'},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
