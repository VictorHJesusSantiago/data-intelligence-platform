"""Ipaas Control 24: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.24",
    family="ipaas",
    title='Ipaas Control 24',
    description='Managed connectors, routes, retries and integration policies',
    operation="derive",
    configuration={'field': 'owner', 'target': 'ipaas_value_24', 'factor': 1.24},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
