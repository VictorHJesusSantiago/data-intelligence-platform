"""Data Governance Control 04: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.04",
    family="data_governance",
    title='Data Governance Control 04',
    description='Classification, stewardship, policy and retention controls',
    operation="derive",
    configuration={'field': 'amount', 'target': 'data_governance_value_04', 'factor': 1.04},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
