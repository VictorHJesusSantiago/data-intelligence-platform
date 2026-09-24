"""Data Governance Control 02: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.02",
    family="data_governance",
    title='Data Governance Control 02',
    description='Classification, stewardship, policy and retention controls',
    operation="filter_not_null",
    configuration={'field': 'owner', 'target': 'data_governance_value_02'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
