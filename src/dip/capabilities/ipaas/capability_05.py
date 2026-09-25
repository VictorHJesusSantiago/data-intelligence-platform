"""Ipaas Control 05: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.05",
    family="ipaas",
    title='Ipaas Control 05',
    description='Managed connectors, routes, retries and integration policies',
    operation="aggregate",
    configuration={'field': 'status', 'target': 'ipaas_value_05'},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
