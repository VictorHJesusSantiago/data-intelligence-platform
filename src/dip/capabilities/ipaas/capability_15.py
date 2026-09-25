"""Ipaas Control 15: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.15",
    family="ipaas",
    title='Ipaas Control 15',
    description='Managed connectors, routes, retries and integration policies',
    operation="aggregate",
    configuration={'field': 'status', 'target': 'ipaas_value_15'},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
