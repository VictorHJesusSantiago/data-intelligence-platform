"""Analytics Control 07: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.07",
    family="analytics",
    title='Analytics Control 07',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="dedupe",
    configuration={'field': 'source', 'target': 'analytics_value_07'},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
