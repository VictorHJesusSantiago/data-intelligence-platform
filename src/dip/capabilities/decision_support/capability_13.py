"""Decision Support Control 13: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.13",
    family="decision_support",
    title='Decision Support Control 13',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="project",
    configuration={'field': 'status', 'target': 'decision_support_value_13', 'fields': ['id', 'status', 'value']},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
