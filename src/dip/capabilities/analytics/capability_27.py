"""Analytics Control 27: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.27",
    family="analytics",
    title='Analytics Control 27',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="dedupe",
    configuration={'field': 'source', 'target': 'analytics_value_27'},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
