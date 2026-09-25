"""Geospatial Analytics Control 01: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.01",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 01',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="profile",
    configuration={'field': 'event_time', 'target': 'geospatial_analytics_value_01'},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
