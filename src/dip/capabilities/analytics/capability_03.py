"""Analytics Control 03: Descriptive, diagnostic, predictive and prescriptive analytical functions."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="analytics.03",
    family="analytics",
    title='Analytics Control 03',
    description='Descriptive, diagnostic, predictive and prescriptive analytical functions',
    operation="project",
    configuration={'field': 'category', 'target': 'analytics_value_03', 'fields': ['id', 'category', 'value']},
    tags=("analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
