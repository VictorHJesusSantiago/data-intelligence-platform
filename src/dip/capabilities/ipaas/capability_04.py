"""Ipaas Control 04: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.04",
    family="ipaas",
    title='Ipaas Control 04',
    description='Managed connectors, routes, retries and integration policies',
    operation="derive",
    configuration={'field': 'owner', 'target': 'ipaas_value_04', 'factor': 1.04},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
