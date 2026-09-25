"""Decision Support Control 06: KPI evaluation, scenarios and explainable recommendations."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="decision_support.06",
    family="decision_support",
    title='Decision Support Control 06',
    description='KPI evaluation, scenarios and explainable recommendations',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'decision_support_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("decision_support", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
