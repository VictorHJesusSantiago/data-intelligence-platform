"""Geospatial Analytics Control 08: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.08",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 08',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="mask",
    configuration={'field': 'value', 'target': 'geospatial_analytics_value_08'},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
