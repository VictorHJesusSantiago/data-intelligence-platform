"""Ipaas Control 03: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.03",
    family="ipaas",
    title='Ipaas Control 03',
    description='Managed connectors, routes, retries and integration policies',
    operation="project",
    configuration={'field': 'category', 'target': 'ipaas_value_03', 'fields': ['id', 'category', 'value']},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
