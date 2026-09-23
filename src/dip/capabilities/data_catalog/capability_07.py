"""Data Catalog Control 07: Asset discovery, metadata enrichment and ownership workflows."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_catalog.07",
    family="data_catalog",
    title='Data Catalog Control 07',
    description='Asset discovery, metadata enrichment and ownership workflows',
    operation="dedupe",
    configuration={'field': 'id', 'target': 'data_catalog_value_07'},
    tags=("data_catalog", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
