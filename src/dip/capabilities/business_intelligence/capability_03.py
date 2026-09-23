"""Business Intelligence Control 03: Business intelligence metrics, scorecards and executive insights."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="business_intelligence.03",
    family="business_intelligence",
    title='Business Intelligence Control 03',
    description='Business intelligence metrics, scorecards and executive insights',
    operation="project",
    configuration={'field': 'event_time', 'target': 'business_intelligence_value_03', 'fields': ['id', 'event_time', 'value']},
    tags=("business_intelligence", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
