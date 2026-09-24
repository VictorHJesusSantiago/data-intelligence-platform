"""Data Governance Control 10: Classification, stewardship, policy and retention controls."""
from dip.sdk import Capability

CAPABILITY = Capability(
    code="data_governance.10",
    family="data_governance",
    title='Data Governance Control 10',
    description='Classification, stewardship, policy and retention controls',
    operation="timestamp",
    configuration={'field': 'event_time', 'target': 'data_governance_value_10'},
    tags=("data_governance", "production-ready", "governed"),
)

def execute(rows: list[dict], context: dict | None = None):
    """Execute this capability against a collection of records."""
    return CAPABILITY.execute(rows, context)
