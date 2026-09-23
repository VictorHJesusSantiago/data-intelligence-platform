"""Analytics Control 24: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.24",
    family="analytics",
    title='Analytics Control 24',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="derive",
    configuration={'field': 'owner', 'target': 'analytics_value_24', 'factor': 1.24},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
