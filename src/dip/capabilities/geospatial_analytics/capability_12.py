"""Geospatial Analytics Control 12: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.12",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 12',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="filter_not_null",
    configuration={'field': 'category', 'target': 'geospatial_analytics_value_12'},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
