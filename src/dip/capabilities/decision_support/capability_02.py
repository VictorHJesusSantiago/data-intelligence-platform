"""Decision Support Control 02: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.02",
    family="decision_support",
    title='Decision Support Control 02',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="filter_not_null",
    configuration={'field': 'owner', 'target': 'decision_support_value_02'},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
