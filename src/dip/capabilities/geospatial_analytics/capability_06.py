"""Geospatial Analytics Control 06: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.06",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 06',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'geospatial_analytics_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
