"""Analytics Control 01: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.01",
    family="analytics",
    title='Analytics Control 01',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="profile",
    configuration={'field': 'email', 'target': 'analytics_value_01'},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
