"""Analytics Control 06: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.06",
    family="analytics",
    title='Analytics Control 06',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'analytics_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
