"""Business Intelligence Control 13: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.13",
    family="business_intelligence",
    title='Business Intelligence Control 13',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="project",
    configuration={'field': 'event_time', 'target': 'business_intelligence_value_13', 'fields': ['id', 'event_time', 'value']},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
