"""Data Catalog Control 22: Asset discovery, metadata enrichment and ownership workflows."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_catalog.22",
    family="data_catalog",
    title='Data Catalog Control 22',
    description='Asset discovery, metadata enrichment and ownership workflows',
    operation="filter_not_null",
    configuration={'field': 'category', 'target': 'data_catalog_value_22'},
    tags=("data_catalog", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
