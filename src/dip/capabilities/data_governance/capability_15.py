"""Data Governance Control 15: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.15",
    family="data_governance",
    title='Data Governance Control 15',
    description='Classification, stewardship, policy and retention controls',
    operation="aggregate",
    configuration={'field': 'source', 'target': 'data_governance_value_15'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
