"""Data Governance Control 09: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.09",
    family="data_governance",
    title='Data Governance Control 09',
    description='Classification, stewardship, policy and retention controls',
    operation="classify",
    configuration={'field': 'email', 'target': 'data_governance_value_09'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
