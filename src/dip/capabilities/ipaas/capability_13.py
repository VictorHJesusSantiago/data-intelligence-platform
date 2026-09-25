"""Ipaas Control 13: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.13",
    family="ipaas",
    title='Ipaas Control 13',
    description='Managed connectors, routes, retries and integration policies',
    operation="project",
    configuration={'field': 'category', 'target': 'ipaas_value_13', 'fields': ['id', 'category', 'value']},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
