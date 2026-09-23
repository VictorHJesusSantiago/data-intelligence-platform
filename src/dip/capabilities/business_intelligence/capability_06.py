"""Business Intelligence Control 06: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.06",
    family="business_intelligence",
    title='Business Intelligence Control 06',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'business_intelligence_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
