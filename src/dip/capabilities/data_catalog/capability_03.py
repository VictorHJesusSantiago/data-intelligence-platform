"""Data Catalog Control 03: Asset discovery, metadata enrichment and ownership workflows."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_catalog.03",
    family="data_catalog",
    title='Data Catalog Control 03',
    description='Asset discovery, metadata enrichment and ownership workflows',
    operation="project",
    configuration={'field': 'owner', 'target': 'data_catalog_value_03', 'fields': ['id', 'owner', 'value']},
    tags=("data_catalog", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
