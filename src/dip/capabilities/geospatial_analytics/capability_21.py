"""Geospatial Analytics Control 21: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.21",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 21',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="profile",
    configuration={'field': 'event_time', 'target': 'geospatial_analytics_value_21'},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
