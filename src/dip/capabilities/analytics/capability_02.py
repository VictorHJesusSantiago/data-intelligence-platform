"""Analytics Control 02: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.02",
    family="analytics",
    title='Analytics Control 02',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="filter_not_null",
    configuration={'field': 'event_time', 'target': 'analytics_value_02'},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
