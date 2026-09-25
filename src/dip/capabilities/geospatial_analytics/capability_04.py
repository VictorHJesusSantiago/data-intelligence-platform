"""Geospatial Analytics Control 04: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.04",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 04',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="derive",
    configuration={'field': 'status', 'target': 'geospatial_analytics_value_04', 'factor': 1.04},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
