"""Ipaas Control 06: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.06",
    family="ipaas",
    title='Ipaas Control 06',
    description='Managed connectors, routes, retries and integration policies',
    operation="validate_range",
    configuration={'field': 'value', 'target': 'ipaas_value_06', 'minimum': 0, 'maximum': 1000006},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
