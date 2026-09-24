"""Data Catalog Control 15: Asset discovery, metadata enrichment and ownership workflows."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_catalog.15",
    family="data_catalog",
    title='Data Catalog Control 15',
    description='Asset discovery, metadata enrichment and ownership workflows',
    operation="aggregate",
    configuration={'field': 'amount', 'target': 'data_catalog_value_15'},
    tags=("data_catalog", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
