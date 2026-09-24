"""Data Governance Control 28: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.28",
    family="data_governance",
    title='Data Governance Control 28',
    description='Classification, stewardship, policy and retention controls',
    operation="mask",
    configuration={'field': 'region', 'target': 'data_governance_value_28'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
