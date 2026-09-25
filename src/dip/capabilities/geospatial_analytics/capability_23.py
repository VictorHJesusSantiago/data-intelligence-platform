"""Geospatial Analytics Control 23: Regional enrichment, location grouping and spatial attributes."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="geospatial_analytics.23",
    family="geospatial_analytics",
    title='Geospatial Analytics Control 23',
    description='Regional enrichment, location grouping and spatial attributes',
    operation="project",
    configuration={'field': 'owner', 'target': 'geospatial_analytics_value_23', 'fields': ['id', 'owner', 'value']},
    tags=("geospatial_analytics", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
