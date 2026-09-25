"""Ipaas Control 01: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.01",
    family="ipaas",
    title='Ipaas Control 01',
    description='Managed connectors, routes, retries and integration policies',
    operation="profile",
    configuration={'field': 'email', 'target': 'ipaas_value_01'},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
