"""Business Intelligence Control 30: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.30",
    family="business_intelligence",
    title='Business Intelligence Control 30',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="timestamp",
    configuration={'field': 'value', 'target': 'business_intelligence_value_30'},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
