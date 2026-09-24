"""Data Catalog Control 13: Asset discovery, metadata enrichment and ownership workflows."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_catalog.13",
    family="data_catalog",
    title='Data Catalog Control 13',
    description='Asset discovery, metadata enrichment and ownership workflows',
    operation="project",
    configuration={'field': 'owner', 'target': 'data_catalog_value_13', 'fields': ['id', 'owner', 'value']},
    tags=("data_catalog", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
