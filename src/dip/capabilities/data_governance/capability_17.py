"""Data Governance Control 17: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.17",
    family="data_governance",
    title='Data Governance Control 17',
    description='Classification, stewardship, policy and retention controls',
    operation="dedupe",
    configuration={'field': 'value', 'target': 'data_governance_value_17'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
