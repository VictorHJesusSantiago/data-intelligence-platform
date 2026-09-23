"""Analytics Control 15: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.15",
    family="analytics",
    title='Analytics Control 15',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="aggregate",
    configuration={'field': 'status', 'target': 'analytics_value_15'},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
