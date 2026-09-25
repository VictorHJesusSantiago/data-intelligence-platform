"""Ipaas Control 17: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.17",
    family="ipaas",
    title='Ipaas Control 17',
    description='Managed connectors, routes, retries and integration policies',
    operation="dedupe",
    configuration={'field': 'source', 'target': 'ipaas_value_17'},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
