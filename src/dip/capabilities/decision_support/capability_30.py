"""Decision Support Control 30: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.30",
    family="decision_support",
    title='Decision Support Control 30',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="timestamp",
    configuration={'field': 'event_time', 'target': 'decision_support_value_30'},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
