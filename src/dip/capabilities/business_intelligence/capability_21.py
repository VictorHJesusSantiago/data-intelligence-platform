"""Business Intelligence Control 21: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.21",
    family="business_intelligence",
    title='Business Intelligence Control 21',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="profile",
    configuration={'field': 'region', 'target': 'business_intelligence_value_21'},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
