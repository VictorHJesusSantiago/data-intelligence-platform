"""Geospatial Analytics Control 09: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.09",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 09',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="classify",
    configuration={'field': 'region', 'target': 'geospatial_analytics_value_09'},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
