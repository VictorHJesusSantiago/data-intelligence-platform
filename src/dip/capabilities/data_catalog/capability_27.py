"""Data Catalog Control 27: Asset discovery, metadata enrichment and ownership workflows."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_catalog.27",
    family="data_catalog",
    title='Data Catalog Control 27',
    description='Asset discovery, metadata enrichment and ownership workflows',
    operation="dedupe",
    configuration={'field': 'id', 'target': 'data_catalog_value_27'},
    tags=("data_catalog", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
