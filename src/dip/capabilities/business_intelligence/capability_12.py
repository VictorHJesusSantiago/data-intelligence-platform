"""Business Intelligence Control 12: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.12",
    family="business_intelligence",
    title='Business Intelligence Control 12',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="filter_not_null",
    configuration={'field': 'email', 'target': 'business_intelligence_value_12'},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
