"""Decision Support Control 22: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.22",
    family="decision_support",
    title='Decision Support Control 22',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="filter_not_null",
    configuration={'field': 'owner', 'target': 'decision_support_value_22'},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
