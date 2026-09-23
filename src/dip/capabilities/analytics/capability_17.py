"""Analytics Control 17: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.17",
    family="analytics",
    title='Analytics Control 17',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="dedupe",
    configuration={'field': 'source', 'target': 'analytics_value_17'},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
