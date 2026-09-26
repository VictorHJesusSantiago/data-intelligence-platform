"""Master Data Management Control 11: Matching, merging and golden-record management."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="master_data_management.11",
    family="master_data_management",
    title='Master Data Management Control 11',
    description='Matching, merging and golden-record management',
    operation="profile",
    configuration={'field': 'status', 'target': 'master_data_management_value_11'},
    tags=("master_data_management", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
