"""Ipaas Control 22: Managed connectors, routes, retries and integration policies."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="ipaas.22",
    family="ipaas",
    title='Ipaas Control 22',
    description='Managed connectors, routes, retries and integration policies',
    operation="filter_not_null",
    configuration={'field': 'event_time', 'target': 'ipaas_value_22'},
    tags=("ipaas", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
