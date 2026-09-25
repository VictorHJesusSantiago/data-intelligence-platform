"""Ipaas Control 08: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.08",
    family="ipaas",
    title='Ipaas Control 08',
    description='Managed connectors, routes, retries and integration policies',
    operation="mask",
    configuration={'field': 'id', 'target': 'ipaas_value_08'},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
