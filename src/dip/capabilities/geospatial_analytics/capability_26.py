"""Geospatial Analytics Control 26: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.26",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 26',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'geospatial_analytics_value_26', 'minimum': 0, 'maximum': 1000026},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
