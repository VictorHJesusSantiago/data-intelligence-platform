"""Business Intelligence Control 24: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.24",
    family="business_intelligence",
    title='Business Intelligence Control 24',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="derive",
    configuration={'field': 'category', 'target': 'business_intelligence_value_24', 'factor': 1.24},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
