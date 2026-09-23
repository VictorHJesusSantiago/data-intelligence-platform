"""Business Intelligence Control 22: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.22",
    family="business_intelligence",
    title='Business Intelligence Control 22',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="filter_not_null",
    configuration={'field': 'email', 'target': 'business_intelligence_value_22'},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
