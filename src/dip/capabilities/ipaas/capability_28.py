"""Ipaas Control 28: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.28",
    family="ipaas",
    title='Ipaas Control 28',
    description='Managed connectors, routes, retries and integration policies',
    operation="mask",
    configuration={'field': 'id', 'target': 'ipaas_value_28'},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
