"""Data Governance Control 27: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.27",
    family="data_governance",
    title='Data Governance Control 27',
    description='Classification, stewardship, policy and retention controls',
    operation="dedupe",
    configuration={'field': 'value', 'target': 'data_governance_value_27'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
